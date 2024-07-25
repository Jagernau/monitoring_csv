import requests
from datetime import datetime 
import typing
import pandas as pd
import re
import new_config
import json

class ScoutTreeData:

    url_base = new_config.SCOUT_TREE_URL
    login = new_config.SCOUT_TREE_LOGIN
    password = new_config.SCOUT_TREE_PASSWORD
    based_token = new_config.SCOUT_TREE_BASED_TOKEN


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

    def conn(self):
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
        for i in available_objects:
            for j in groups_with_objects:
                if i["id"] in j["unitIds"]:

                    result.append(
                            f"объект {i['name']} {i['id']} - группа {j['groupName']} {j['id']}\n"
                            )

        #save to txt
        with open('scout_365_data.txt', 'w', encoding='utf-8') as f:
            f.write('\n'.join(result))

        return [available_objects, groups_and_parents, groups_with_objects]


scout_tree = ScoutTreeData()
data = scout_tree.conn()
# save to json
with open('scout_365_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

