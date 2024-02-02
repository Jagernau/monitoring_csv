import requests
from params import presp
import typing
import pandas as pd
import re

class FortData:
    """
    Класс для работы с API Форт
    """
    def __init__(self) -> None:

            self.params = dict()
            self.params = presp()
            self.companies = dict()
            self.data = list()

    def __conn(self) -> typing.List:
        """
        Делает выгрузку из системы мониторинга Форт
        """
        url_base = self.params["12"]["url_base"]
        api_cmd = self.params["12"]["api_cmd"]
        headers = self.params["12"]["headers"]
        params = self.params["12"]["params"]

        resp = requests.get(url_base + api_cmd, headers=headers, params=params)

        Session_Id = resp.headers["SessionId"]

        url_base = self.params["1201"]["url_base"]
        api_cmd = self.params["1201"]["api_cmd"]
        headers = self.params["1201"]["headers"]
        headers["SessionId"] = Session_Id
        payload = self.params["1201"]["payload"]
        payload["companyId"] = 0

        resp = requests.get(url_base + api_cmd, headers=headers, params=payload)

        rlist = dict()
        rlist = resp.json()

        self.companies["companies"] = rlist["companies"]

        url_base = self.params["1202"]["url_base"]
        api_cmd = self.params["1202"]["api_cmd"]
        headers = self.params["1202"]["headers"]
        headers["SessionId"] = Session_Id
        payload = self.params["1202"]["payload"]

        for el in self.companies["companies"]:
            payload["companyId"] = el["id"]  # ell
            resp = requests.get(url_base + api_cmd, headers=headers, params=payload)

            rlist = resp.json()

            for e in rlist["objects"]:
                e["uid"] = el["id"]
                e["unm"] = el["name"]
                self.data.append(e)

        res = self.data

        return res


    def list_to_csv(self) -> None:
        """
        Формирует CSV файл из json Fort, адаптирует под Ромину бд
        """
        data = self.__conn()
        for item in data:
            item["unm"] = re.sub("[^0-9a-zA-ZА-я-_]+", " ", item["unm"])
            item["name"] = " " + re.sub("[^0-9a-zA-ZА-я-_]+", " ", item["name"])
            item["uid"] = " " + str(item["uid"])
            item["id"] = " " + str(item["id"])
        df = pd.DataFrame(data)
        df =  df[['unm', 'uid', 'name', 'id']]
        df['Days Active'] = ' Да'
        df.insert(2, 'Monitoring System ID',' 12')
        df.columns = ['Учётка', 'ID Учётки', 'ID Системы', 'Имя объекта', 'ID Объекта', "Активность"]
        df.to_csv('fort.csv', index=False)

