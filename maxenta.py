import requests
import pandas as pd
import re
import config
import help_funcs
from my_logger import logger
from database import crud
import json

class AxentaData:

    def __init__(self):
        self.url_base = config.AXENTA_URL

    def __token(self, login, password):
        "Вход в аксенту, логин"
        url = f'{self.url_base}auth/login/'
        data = {'username': login, 'password': password}
        headers = {'Accept': 'application/json'}
        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 200:
            return response.json()["token"]
        else:
            return None

    def __get_objs(self, token):
        "Список объектов"
        token = token
        obj_url = f"{self.url_base}objects/"
        headers = {'Authorization': f'Token {token}', 'Accept': 'application/json'}
        all_objs = requests.get(obj_url, headers=headers)
        if all_objs.status_code == 200:
            return all_objs.json()

    def __conn(self):
        "Получение данных из СМ"
        all_loggins = crud.get_mysql_logins()
        final_result = []
        for login in all_loggins:
            token = self.__token(login=login[0], password=login[1])
            if token:
                objects = self.__get_objs(token)
                if not objects:
                    logger.error(f'Не получены объекты из AXENTA')
                for obj in objects:
                    final_result.append([
                            re.sub("[^0-9a-zA-ZА-я-_]+", " ", login[0]), # Имя группы
                            " " + str(login[2]), # Группа ID
                            " 18", # Мониторинг система ID
                            " " + re.sub("[^0-9a-zA-ZА-я-_]+", " ", obj["name"]), # Объект имя
                            " " + str(obj["id"]), # Объект ID
                            " Да", # Активность
                            ])
        return final_result


    def list_to_csv(self):
        data = self.__conn()
        df = pd.DataFrame(data)
        df.columns = ['Учётка', 'ID Учётки', 'ID Системы', 'Имя объекта', 'ID Объекта', "Активность"]
        df.to_csv('axenta.csv', index=False)

        list_obj = []
        for i in data:
            list_obj.append(
                    [
                        str(i[0]),
                        i[1],
                        "18",
                        str(i[3]),
                        i[4],
                        " Да",
                    ]
                    )
        #блок логирования успешности добавления объектов
        try:
            crud.add_objects(list_obj)
            logger.info("Объекты из axenta закончили соединение с базой данных")
        except Exception as e:
            logger.error(f"В добавлении в базу данных объектов из axenta возникла ошибка: {e}")

