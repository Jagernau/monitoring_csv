import requests
import typing
import pandas as pd
import re

from database import crud
from my_logger import logger
import config

class FortData:
    """
    Класс для работы с API Форт
    """
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    payload: dict[str, typing.Any] = {"companyId": 0}

    url_auth = str(config.FORT_HOST) + "/api/integration/v1/connect"
    url_companies_list = str(config.FORT_HOST) + "/api/integration/v1/getcompanieslist"
    url_objects = str(config.FORT_HOST) + "/api/integration/v1/getobjectslist"

    def get_data(self) -> typing.List:
        """
        Делает выгрузку из системы мониторинга Форт
        """

        resp_session_id = requests.get(self.url_auth, headers=self.headers, params={
            "login": str(config.FORT_LOGIN),
            "password": str(config.FORT_PASSWORD),
            "lang": "ru-ru",
            "timezone": "+3",
            })
        # добавляем в шапку токен
        token = resp_session_id.headers["SessionId"]
        self.headers["SessionId"] = str(token)
        # добавляем в payload токен
        self.payload["SessionId"] = str(token)

        companies = requests.get(self.url_companies_list, headers=self.headers, params=self.payload).json()["companies"]

        data = list()

        for el in companies:
            self.payload["companyId"] = el["id"]
            objects = requests.get(
                    self.url_objects, 
                    headers=self.headers, 
                    params=self.payload
                    ).json()["objects"]

            for e in objects:
                e["uid"] = el["id"]
                e["unm"] = el["name"]
                data.append(e)

        return data


    def list_to_csv(self) -> None:
        """
        Формирует CSV файл из json Fort, адаптирует под Ромину бд
        """
        data = self.get_data()
        for item in data:
            item["unm"] = re.sub("[^0-9a-zA-ZА-я-_]+", " ", item["unm"])
            item["name"] = " " + re.sub("[^0-9a-zA-ZА-я-_]+", " ", item["name"])
            item["uid"] = str(item["uid"])
            item["id"] = str(item["id"])
        df = pd.DataFrame(data)
        df =  df[['unm', 'uid', 'name', 'id']]
        df['Days Active'] = ' Да'
        df.insert(2, 'Monitoring System ID',' 12')
        df.columns = ['Учётка', 'ID Учётки', 'ID Системы', 'Имя объекта', 'ID Объекта', "Активность"]

        df.to_csv('fort.csv', index=False)

        list_obj = []
        for i in data:
            list_obj.append(
                    [
                        str(i["unm"]),
                        i["uid"],
                        "12",
                        i["name"],
                        i["id"],
                        " Да",
                    ]
                    )
        try:
            crud.add_objects(list_obj)
            logger.info("Объекты из fort добавлены в базу данных")
            
        except Exception as e:
            logger.error(f"В добавлении в базу данных объектов из fort возникла ошибка: {e}")

