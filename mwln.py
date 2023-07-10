from wialon.sdk import WialonSdk
from params import presp
import json
import typing
import pandas as pd
import re

class WialonData:
    """
    Класс для работы с API Wialon
    """
    def __init__(self) -> None:

            self.params = dict()
            self.params = presp()
            self.companies = dict()
            self.data = list()

    def __conn(self):

        sdk = WialonSdk(
            is_development=self.params["11"]["WialonSdk"]["is_development"],
            scheme=self.params["11"]["WialonSdk"]["scheme"],
            host=self.params["11"]["WialonSdk"]["host"],
            port=self.params["11"]["WialonSdk"]["port"],
            session_id=self.params["11"]["WialonSdk"]["session_id"],
            extra_params=self.params["11"]["WialonSdk"]["extra_params"],
        )

        token = self.params["11"]["token"]
        response = sdk.login(token)
        parameters = self.params["11"]["Parameters"]["user"]
        users = sdk.core_search_items(parameters)

        parameters = self.params["11"]["Parameters"]["avl_unit"]
        units = sdk.core_search_items(parameters)

        # self.data = units['items']

        sdk.logout()

        res = {"objects": units["items"], "users": users["items"]}


        return res

    def dict_to_csv(self):
        data = self.__conn()
        objects = data["objects"]
        users = data["users"]
        for obj in objects:
            if obj["act"] == 0:
                obj["act"] = " Нет"
            if obj["act"] == 1:
                obj["act"] = " Да"
            obj["nm"] = " " + re.sub("[^0-9a-zA-ZА-я-_]+", " ", obj["nm"])

            for usr in users:
                if obj["crt"] == usr["id"]:
                    obj["client"] = re.sub("[^0-9a-zA-ZА-я-_]+", " ", usr["nm"])
        
        for item in objects:
            item["crt"] = " " + str(item["crt"])
            item["id"] = " " + str(item["id"])

        df = pd.DataFrame(objects)
        df =  df[['client', 'crt', 'nm', 'id', "act"]]
        df.insert(2, 'Monitoring System ID',' 11')
        df.columns = ['Учётка', 'ID Учётки', 'ID Системы', 'Имя объекта', 'ID Объекта', "Активность"]
        df.to_csv('wialon.csv', index=False)

wialon = WialonData()
wialon.dict_to_csv()
