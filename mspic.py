#Закоментируй код, сделай typing, сделай коментарии
import requests
from datetime import datetime
from params import presp
import typing
import pandas as pd
import re
from database import crud
from my_logger import logger

class ScautData:
    """ 
    Класс для работы с API Скаут
    """

    def __init__(self) -> None:

            self.params = dict()
            self.params = presp()
            self.companies = dict()
            self.data = list()

    def __conn(self) -> typing.List:
        """
        Делает выгрузку из системы мониторинга Скаут
        """


        url_base = self.params["14"]["url_base"]
        api_cmd = self.params["14"]["api_cmd"]
        headers = self.params["14"]["headers"]
        params = self.params["14"]["params"]

        dt = datetime.now()
        ts = datetime.timestamp(dt)
        ts = int(ts)

        params["TimeStampUtc"] = "/Date(" + str(ts) + ")/"

        resp = requests.post(url_base + api_cmd, json=params)

        AuthKey = resp.json()["SessionId"]
        resp.close()
        url_base = self.params["14"]["url_base"]
        api_cmd = self.params["1401"]["api_cmd"]
        headers["ScoutAuthorization"] = AuthKey

        resp = requests.get(url_base + api_cmd, headers=headers)

        rlist = resp.json()
        resp.close()
        self.companies["companies"] = rlist

        d0 = self.params["1401"]["unitGroups"]["d0"]
        l0 = self.params["1401"]["unitGroups"]["l0"]
        d1 = self.params["1401"]["unitGroups"]["d1"]
        units = rlist[d0][l0][d1]
        url_base = self.params["14"]["url_base"]
        api_cmd = self.params["1402"]["api_cmd"]
        params = self.params["1402"]["params"]

        for el in units:
            params["Requests"].append({"ObjectId": el})

        headers["ScoutAuthorization"] = AuthKey

        resp = requests.post(url_base + api_cmd, headers=headers, json=params)

        rlist = resp.json()
        resp.close()
        self.data = rlist["Units"]

        res = self.data

        return res


    def list_to_csv(self) -> None:
        """
        Формирует CSV файл из json Скаут, адаптированный под Ромину бд
        """
        data = self.__conn()
        for item in data:
            item["Description"] = re.sub("[^0-9a-zA-ZА-я-_]+", " ", item["Description"])
            item["Name"] = " " + re.sub("[^0-9a-zA-ZА-я-_]+", " ", item["Name"])
            item["UnitId"] = " " + str(item["UnitId"])
            
        df = pd.DataFrame(data)
        df = df[['Description', 'CompanyId', 'Name', 'UnitId']]
        df['Days Active'] = ' Да'
        df.insert(2, 'Monitoring System ID',' 14')
        company_id = " " + df['CompanyId'].astype(str) + df['Description']
        df['CompanyId'] = company_id
        df.columns = ['Учётка', 'ID Учётки', 'ID Системы', 'Имя объекта', 'ID Объекта', "Активность"]

        df.to_csv('scaut.csv', index=False)


        list_obj = []
        for i in data:

            client_name = i.get('Description', 'Неработает_тест')
            list_obj.append(
                    [
                        str(client_name),
                        i["CompanyId"],
                        " 14",
                        i["Name"],
                        i["UnitId"],
                        " Да",
                    ]
                    )
        try:
            crud.add_objects(list_obj)
            logger.info("Объекты из scaut добавлены в базу данных")
        except Exception as e:
            logger.error(f"В добавлении в базу данных объектов из scaut возникла ошибка: {e}")

