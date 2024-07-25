import requests
from datetime import datetime 
import typing
import pandas as pd
import re
import new_config

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

    def __conn(self):
        """
        Делает выгрузку из системы мониторинга ScoutTree
        """

        




