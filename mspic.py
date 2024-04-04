import requests
from datetime import datetime
import typing
import pandas as pd
import re
from database import crud
from my_logger import logger
import config

class ScautData:
    """ 
    Класс для работы с API Скаут
    """ 
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    url_auth = str(config.SCAUT_HOST) + "/spic/auth/rest/Login"
    url_companies = str(config.SCAUT_HOST) + "/spic/unitGroups/rest/"
    url_units = str(config.SCAUT_HOST) + "/spic/units/rest/getUnits"
    
    params = {
        "Login": config.SCAUT_LOGIN,
        "Password": config.SCAUT_PASSWORD,
        "TimeStampUtc": "/Date(" + str(int(datetime.timestamp(datetime.now()))) + ")/",
        "TimeZoneOlsonId": "Europe/Moscow",
        "CultureName": "ru-ru",
        "UiCultureName": "ru-ru",
    }

    def get_data(self) -> typing.List:
        """
        Делает выгрузку из системы мониторинга Скаут
        """

        resp_session_id = requests.post(self.url_auth, headers=self.headers, json=self.params)

        self.headers["ScoutAuthorization"] = resp_session_id.json()["SessionId"]
        resp_session_id.close()

        resp_companies = requests.get(self.url_companies, headers=self.headers)
        companies = resp_companies.json()
        resp_companies.close()

        units_ids = companies["Groups"][int(0)]["UnitIds"]
        self.params["Requests"] = []

        for item in units_ids:
            self.params["Requests"].append({"ObjectId": item})

        resp_units = requests.post(
                self.url_units, 
                headers=self.headers, 
                json=self.params)

        data = resp_units.json()["Units"]
        resp_units.close()

        for item in data:
            item["Description"] = re.sub("[^0-9a-zA-ZА-я-_]+", " ", item["Description"])
            item["Name"] = " " + re.sub("[^0-9a-zA-ZА-я-_]+", " ", item["Name"])
            item["UnitId"] = str(item["UnitId"])

        return data

    @staticmethod
    def data_to_csv(data: typing.List) -> None:
        """
        Формирует CSV файл из json Скаут, адаптированный под Ромину бд
        """
            
        df = pd.DataFrame(data)
        df = df[['Description', 'CompanyId', 'Name', 'UnitId']]
        df['Days Active'] = ' Да'
        df.insert(2, 'Monitoring System ID',' 14')
        company_id = " " + df['CompanyId'].astype(str) + df['Description']
        df['CompanyId'] = company_id
        df.columns = ['Учётка', 'ID Учётки', 'ID Системы', 'Имя объекта', 'ID Объекта', "Активность"]

        df.to_csv('scaut.csv', index=False)


    @staticmethod
    def add_to_db(data: typing.List) -> None:
        list_obj = []
        for i in data:

            if i["Description"] == "":
                client_name = 'Неработает_тест'
            else:
                client_name = i["Description"]
            companys_id = " " + str(i['CompanyId']) + i['Description']

            list_obj.append(
                    [
                        str(client_name),
                        str(companys_id),
                        "14",
                        i["Name"],
                        i["UnitId"],
                        " Да",
                    ]
                    )
        crud.add_objects(list_obj)


    def __str__(self) -> str:
        return str("scaut")