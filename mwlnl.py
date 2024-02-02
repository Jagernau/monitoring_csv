from wialon.sdk import WialonSdk
from params import presp
import params
import re
import json
import pandas as pd


class WlocalData:
    def __init__(self):

            self.params = dict()
            self.params = presp()
            self.companies = dict()
            self.data = list()


    def __conn(self):

        # Initialize Wialon instance
            sdk = WialonSdk(
                is_development=self.params["1101"]["WialonSdk"]["is_development"],
                scheme=self.params["1101"]["WialonSdk"]["scheme"],
                host=self.params["1101"]["WialonSdk"]["host"],
                port=self.params["1101"]["WialonSdk"]["port"],
                session_id=self.params["1101"]["WialonSdk"]["session_id"],
                extra_params=self.params["1101"]["WialonSdk"]["extra_params"],
            )

            token = self.params["1101"]["token"]
            response = sdk.login(token)
            parameters = self.params["1101"]["Parameters"]["user"]
            users = sdk.core_search_items(parameters)

            parameters = self.params["1101"]["Parameters"]["avl_unit"]
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
        df["crt"] = df["crt"].astype(str)
        df.insert(2, 'Monitoring System ID',' 16')
        df.columns = ['Учётка', 'ID Учётки', 'ID Системы', 'Имя объекта', 'ID Объекта', "Активность"]
        df.to_csv('wlocal.csv', index=False)

