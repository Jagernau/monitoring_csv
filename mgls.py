import requests
import time
from params import presp
import typing
import pandas as pd
import re


class GlanassData:
    """
    Класс для работы с API GlanasSoft
    """
    def __init__(self) -> None:

            self.params = dict()
            self.params = presp()
            self.companies = dict()
            self.data = list()

    def __conn(self) -> typing.List:
        """
        Делает выгрузку из системы мониторинга GlanasSoft
        """

        url_base = self.params["13"]["url_base"]
        api_cmd = self.params["13"]["api_cmd"]
        headers = self.params["13"]["headers"]
        params = self.params["13"]["params"]
        response = requests.post(url_base + api_cmd, headers=headers, json=params)
        AuthKey = response.json()

        url_base = self.params["1301"]["url_base"]
        api_cmd = self.params["1301"]["api_cmd"]
        headers = self.params["1301"]["headers"]
        headers["X-Auth"] = AuthKey["AuthId"]

        response = requests.get(url_base + api_cmd, headers=headers)
        rlist = response.json()
        self.companies["companies"] = rlist

        url_base = self.params["1302"]["url_base"]
        api_cmd = self.params["1302"]["api_cmd"]
        headers = self.params["1302"]["headers"]
        headers["X-Auth"] = AuthKey["AuthId"]
        params = self.params["1302"]["params"]

        params["parentId"] = "80eb1587-12cf-44d4-b0d0-c09b7ddf6110"
        time.sleep(2)
        response = requests.post(
            url_base + api_cmd,
            headers=headers,
            json={"parentId": "80eb1587-12cf-44d4-b0d0-c09b7ddf6110"},
        )
        rlist = response.json()

        for e in rlist:

            self.data.append(
                {
                    "uid": e["parentId"],
                    "unm": e["parentName"],
                    "nm": e["name"],
                    "oid": e["vehicleId"],
                    "gid": e["parentId"],
                    "imei": e["imei"],
                }
            )

        res = self.data

        return res


    def list_to_csv(self) -> None:
        """
        Формирует CSV файл из json Glanass,  адаптированный под Ромину бд
        """
        data = self.__conn()
        for item in data:
            item["unm"] = re.sub("[^0-9a-zA-ZА-я-_]+", " ", item["unm"])
            item["nm"] = " " + re.sub("[^0-9a-zA-ZА-я-_]+", " ", item["nm"])
            item["uid"] = " " + str(item["uid"])
            item["oid"] = " " + str(item["oid"])
            
        df = pd.DataFrame(data)
        df =  df[['unm', 'uid', 'nm', 'oid']]
        df['Days Active'] = ' Да'
        df["unm"] = df["unm"].astype(str)
        df.insert(2, 'Monitoring System ID',' 13')
        df.columns = ['Учётка', 'ID Учётки', 'ID Системы', 'Имя объекта', 'ID Объекта', "Активность"]
        df.to_csv('glonqssoft.csv', index=False)

