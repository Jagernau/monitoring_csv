from dotenv import load_dotenv
import os

load_dotenv()


def presp():

    pconn = {
        "14": {
            "url_base": os.getenv("14_URL"),
            "api_cmd": "/spic/auth/rest/Login",
            "params": {
                "Login": os.getenv("14_LOGIN"),
                "Password": os.getenv("14_PASSWORD"),
                "TimeStampUtc": "_replace",
                "TimeZoneOlsonId": "Europe/Moscow",
                "CultureName": "ru-ru",
                "UiCultureName": "ru-ru",
            },
            "headers": {
                "Content-Type": "application/json",
                "Accept": "json",
                "ScoutAuthorization": "_replace",
            },
        },
        "1401": {
            "api_cmd": "/spic/unitGroups/rest/",
            "unitGroups": {"d0": "Groups", "l0": 0, "d1": "UnitIds"},
        },
        "1402": {"api_cmd": "/spic/units/rest/getUnits", "params": {"Requests": []}},
        "15": {
            "url_base": "monitoring.aoglonass.ru",
            "url_port": os.getenv("15_PORT"),
            "params": {"login": os.getenv("15_LOGIN"), "pwd": os.getenv("15_PASSWORD")},
            "long_session": True,
        },
    }

    return pconn
