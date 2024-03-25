from wialon.sdk import WialonSdk
import re
import pandas as pd

from database import crud
from my_logger import logger
import config

class WlocalData:
    
    """
    Класс для работы с API Wialon local
    """
    user_parametrs = {
                    "spec": {
                        "itemsType": "user",
                        "propName": "sys_name",
                        "propValueMask": "*",
                        "sortType": "sys_name",
                        "or_logic": 0
                    },
                    "force": 1,
                    "flags": 265,
                    "from": 0,
                    "to": 0
    }

    objects_parametrs = {
                        "spec": {
                            "itemsType": "avl_unit",
                            "propName": "sys_name,rel_user_creator_name",
                            "propValueMask": "*,*",
                            "sortType": "sys_name,rel_user_creator_name",
                            "or_logic": 0
                        },
                        "force": 1,
                        "flags": 269,
                        "from": 0,
                        "to": 0
    }
    
    def get_data(self):

        sdk = WialonSdk(
            is_development=True, 
            scheme='https',
            host=str(config.WIALON_LOCAL_HOST),
            port=0,
            session_id='',
            extra_params=""
        )

        response = sdk.login(str(config.WIALON_LOCAL_TOKEN))
        users = sdk.core_search_items(self.user_parametrs)

        units = sdk.core_search_items(self.objects_parametrs)

        sdk.logout()

        data = {"objects": units["items"], "users": users["items"]}


        return data

    def dict_to_csv(self):
        data = self.get_data()
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
            item["crt"] = str(item["crt"])
            item["id"] = str(item["id"])
 
        df = pd.DataFrame(objects)
        df =  df[['client', 'crt', 'nm', 'id', "act"]]
        df["crt"] = df["crt"].astype(str)
        df.insert(2, 'Monitoring System ID',' 16')
        df.columns = ['Учётка', 'ID Учётки', 'ID Системы', 'Имя объекта', 'ID Объекта', "Активность"]
        df.to_csv('wlocal.csv', index=False)

        list_obj = [] #сам список
        #цикл по словарю для пермещения в list_obj
        for i in objects:
            client_name = i.get('client', 'Неработает_тест')
            list_obj.append(
                    [
                        client_name,
                        i["crt"],
                        "16",
                        i["nm"],
                        i["id"],
                        i["act"],
                    ]
                    )
        try:
            crud.add_objects(list_obj)
            logger.info("Объекты из wlocal добавлены в базу данных")

        except Exception as e:
            logger.error(f"В добавлении в базу данных объектов из wlocal возникла ошибка: {e}")

