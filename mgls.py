import requests
import time
import typing
import pandas as pd
import re

from database import crud
from my_logger import logger
import config

class GlanassData:
    """
    Класс для работы с API GlanasSoft
    """

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    url_auth = "https://hosting.glonasssoft.ru/api/v3/auth/login"
    url_agents = "https://hosting.glonasssoft.ru/api/agents"
    url_vehicles = "https://hosting.glonasssoft.ru/api/v3/vehicles/find"


    def get_data(self) -> typing.List:
        """
        Делает выгрузку из системы мониторинга GlanasSoft
        """

        auth_response = requests.post(
                self.url_auth,
                headers=self.headers,
                json={
                    "login": str(config.GLONASS_LOGIN),
                    "password": str(config.GLONASS_PASSWORD),
                    },
                )

        self.headers["X-Auth"] = auth_response.json()["AuthId"] 

        time.sleep(2)
        response = requests.post(
            self.url_vehicles,
            headers=self.headers,
            json={"parentId": "80eb1587-12cf-44d4-b0d0-c09b7ddf6110"},
        )
        vehicles = response.json()

        data = list()

        for e in vehicles:

            data.append(
                {
                    "uid": e["parentId"],
                    "unm": e["parentName"],
                    "nm": e["name"],
                    "oid": e["vehicleId"],
                    "gid": e["parentId"],
                }
            )

        return data


    def list_to_csv(self) -> None:
        """
        Формирует CSV файл из json Glanass,  адаптированный под Ромину бд
        """
        data = self.get_data()
        for item in data:
            item["unm"] = re.sub("[^0-9a-zA-ZА-я-_]+", " ", item["unm"])
            item["nm"] = " " + re.sub("[^0-9a-zA-ZА-я-_]+", " ", item["nm"])
            item["uid"] = " " + str(item["uid"])
            item["oid"] = str(item["oid"])
            
        df = pd.DataFrame(data)
        df =  df[['unm', 'uid', 'nm', 'oid']]
        df['Days Active'] = ' Да'
        df["unm"] = df["unm"].astype(str)
        df.insert(2, 'Monitoring System ID',' 13')
        df.columns = ['Учётка', 'ID Учётки', 'ID Системы', 'Имя объекта', 'ID Объекта', "Активность"]

        df.to_csv('glonqssoft.csv', index=False)

        list_obj = []
        for i in data:
            list_obj.append(
                    [
                        str(i["unm"]),
                        i["uid"],
                        "13",
                        i["nm"],
                        i["oid"],
                        " Да",
                    ]
                    )
        #блок логирования успешности добавления объектов
        try:
            crud.add_objects(list_obj)
            logger.info("Объекты из glanass добавлены в базу данных")
        except Exception as e:
            logger.error(f"В добавлении в базу данных объектов из glanass возникла ошибка: {e}")


