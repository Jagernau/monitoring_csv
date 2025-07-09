import requests
import pandas as pd
import re
import config
import help_funcs
from my_logger import logger
from database import crud


class ScoutTreeData:

    url_base = config.SCOUT_TREE_URL
    login = config.SCOUT_TREE_LOGIN
    password = config.SCOUT_TREE_PASSWORD
    based_token = config.SCOUT_TREE_BASED_TOKEN


    def __token(self):
        """
        Login to Scout_365
        Get access_token
        """
        url = f'{self.url_base}auth/token'
        data = {
                'grant_type': 'password',
                'username': self.login,
                'password': self.password,
                'locale': 'ru-RU',
                'zoneinfo': 'Europe/Moscow'
        }
        headers = {
                'Accept': 'application/json',
                'Authorization': f'Basic {self.based_token}',
                'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = requests.post(url, data=data, headers=headers)
        if response.status_code == 200:
            return response.json()["access_token"]
        else:
            return None

    def __conn(self):
        """
        Делает выгрузку из системы мониторинга ScoutTree
        """
        url_available_objects = f"{self.url_base}v3/units/units-previews"
        url_groups_and_parents = f"{self.url_base}v3/units/scope-with-parents"
        url_groups_with_objects = f"{self.url_base}v3/units/unit-group-ids"

        token = self.__token()

        headers = {
            "Content-Type": "application/json, text/json",
            "Authorization": f"Bearer {token}",
        }

        # Все доступные объекты
        # Так как нет лицензии, приходится использовать этот метод
        response_available_objects = requests.get(url_available_objects, headers=headers)
        available_objects = response_available_objects.json()
        
        # Группы и родители
        response_groups_and_parents = requests.get(url_groups_and_parents, headers=headers)
        groups_and_parents = response_groups_and_parents.json()

        # Группы с объектами
        response_groups_with_objects = requests.get(url_groups_with_objects, headers=headers)
        groups_with_objects = response_groups_with_objects.json()


        # Удаляем группу Сантел
        for group in groups_with_objects:
            if group["id"] == 3668:
                groups_with_objects.remove(group)

        result = []
        # объекты
        for i in available_objects:
            # группы
            for j in groups_with_objects:
                if i["id"] in j["unitIds"]:

                    # Находимируемся по дереву и ищем самую дочернюю
                    deepest_group = help_funcs.find_child_group(groups_and_parents, j["id"])
                    # Если нет дочерних групп, то это самая дочерняя
                    # Исключаем Родителей
                    # Если у подразделения есть дочернее подразделение, но объект находится в родительской, программа не увидит объект
                    if deepest_group is None:

                        result.append([
                                re.sub("[^0-9a-zA-ZА-я-_]+", " ", j["groupName"]), # Имя группы
                                " " + str(j["id"]), # Группа ID
                                " 17", # Мониторинг система ID
                                " " + re.sub("[^0-9a-zA-ZА-я-_]+", " ", i["name"]), # Объект имя
                                " " + str(i["id"]), # Объект ID
                                " Да", # Активность
                                ])
        return result


    def list_to_csv(self):
        data = self.__conn()
        df = pd.DataFrame(data)
        df.columns = ['Учётка', 'ID Учётки', 'ID Системы', 'Имя объекта', 'ID Объекта', "Активность"]
        df.to_csv('scout_tree.csv', index=False)

        list_obj = []
        for i in data:
            list_obj.append(
                    [
                        str(i[0]),
                        i[1],
                        "17",
                        str(i[3]),
                        i[4],
                        " Да",
                    ]
                    )
        #блок логирования успешности добавления объектов
        try:
            crud.add_objects(list_obj)
            logger.info("Объекты из scout_tree закончили соединение с базой данных")
        except Exception as e:
            logger.error(f"В добавлении в базу данных объектов из scout_tree возникла ошибка: {e}")


