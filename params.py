from dotenv import load_dotenv
import os

load_dotenv()

code = {
    "wln": {"wln": "11", "user": "01", "obj": "02"},
    "frt": {"frt": "12", "user": "01", "obj": "02"},
    "gls": {"gls": "13", "user": "01", "obj": "02"},
    "sct": {"sct": "14", "user": "01", "obj": "02"},
    "era": {"era": "15", "user": "01", "obj": "02"},
}


def presp():

    pconn = {
        "11": {
            "WialonSdk": {
                "is_development": True,
                "scheme": "https",
                "host": "hst-api.wialon.com",
                "port": 0,
                "session_id": "",
                "extra_params": "",
            },
            "cid": os.getenv("11_CID"),
            "token": os.getenv("11_TOKEN"),
            "Parameters": {
                "avl_unit": {
                    "spec": {
                        "itemsType": "avl_unit",
                        "propName": "sys_name,rel_user_creator_name",  # "sys_name",
                        "propValueMask": "*,*",
                        "sortType": "sys_name,rel_user_creator_name",
                        "or_logic": 0
                    },
                    "force": 1,
                    "flags": 269,  # 'base flag+advanced properties+custom fields' #2097153, #
                    "from": 0,
                    "to": 0
                },
                "user": {
                    "spec": {
                        "itemsType": "user",
                        "propName": "sys_name",  # "list,propitemname",  # "sys_name",
                        "propValueMask": "*",
                        "sortType": "sys_name",
                        "or_logic": 0
                    },
                    "force": 1,
                    "flags": 265,  # 'base flag+advanced properties+custom fields' #2097153, #
                    "from": 0,
                    "to": 0
                },
                "avl_retranslator": {
                    "spec": {
                        "itemsType": "avl_retranslator",
                        "propName": "retranslator_units",  # "sys_name",
                        "propValueMask": "*,*",
                        "sortType": "retranslator_units",
                        "propType": "propitemname",
                        "or_logic": 0
                    },
                    "force": 1,
                    "flags": 265,  # 'base flag+advanced properties+custom fields' #2097153, #
                    "from": 0,
                    "to": 0
                },
            },
        },
        "1101": {
            "WialonSdk": {
                "is_development": True,
                "scheme": "https",
                "host": "suntel-wialon.ru",
                "port": 0,
                "session_id": "",
                "extra_params": "",  # {}
            },
            "cid": os.getenv("16_CID"),
            "token": os.getenv("16_TOKEN"),
            "Parameters": {
                "avl_unit": {
                    "spec": {
                        "itemsType": "avl_unit",
                        "propName": "sys_name,rel_user_creator_name",  # "sys_name",
                        "propValueMask": "*,*",
                        "sortType": "sys_name,rel_user_creator_name",
                        "or_logic": 0,
                    },
                    "force": 1,
                    "flags": 269,  # 'base flag+advanced properties+custom fields' #2097153, #
                    "from": 0,
                    "to": 0,
                },
                "user": {
                    "spec": {
                        "itemsType": "user",
                        "propName": "sys_name",  # "list,propitemname",  # "sys_name",
                        "propValueMask": "*",
                        "sortType": "sys_name",
                        "or_logic": 0,
                    },
                    "force": 1,
                    "flags": 265,  # 'base flag+advanced properties+custom fields' #2097153, #
                    "from": 0,
                    "to": 0,
                },
                "avl_retranslator": {
                    "spec": {
                        "itemsType": "avl_retranslator",
                        "propName": "retranslator_units",  # "sys_name",
                        "propValueMask": "*,*",
                        "sortType": "retranslator_units",
                        "propType": "propitemname",
                        "or_logic": 0,
                    },
                    "force": 1,
                    "flags": 265,  # 'base flag+advanced properties+custom fields' #2097153, #
                    "from": 0,
                    "to": 0,
                },
            },
        },
        "12": {
            "headers": {
                "Content-Type": "application/json",
                "Accept": "application/json",
            },
            "params": {
                "login": os.getenv("12_LOGIN"),
                "password": os.getenv("12_PASSWORD"),
                "lang": "ru-ru",
                "timezone": "+3",
            },
            "url_base": "https://fm.suntel-nn.ru",
            "api_cmd": "/api/integration/v1/connect",
        },
        "1201": {
            "headers": {
                "SessionId": "_replace",
                "Content-Type": "application/json",
                "Accept": "application/json",
            },
            "payload": {"SessionId": "_replace", "companyId": 0},
            "url_base": "https://fm.suntel-nn.ru",
            "api_cmd": "/api/integration/v1/getcompanieslist",
        },
        "1202": {
            "headers": {
                "SessionId": "_replace",
                "Content-Type": "application/json",
                "Accept": "application/json",
            },
            "payload": {"SessionId": "_replace", "companyId": 0},
            "url_base": "https://fm.suntel-nn.ru",
            "api_cmd": "/api/integration/v1/getobjectslist",
        },
        "13": {
            "url_base": "https://hosting.glonasssoft.ru/api/v3",
            "api_cmd": "/auth/login",
            "params": {"login": os.getenv("13_LOGIN"), "password": os.getenv("13_PASSWORD")},
            "headers": {
                "Content-Type": "application/json",
                "Accept": "application/json",
                "X-Auth": "_replace",
            },
        },
        "1301": {
            "url_base": "https://hosting.glonasssoft.ru/api",
            "api_cmd": "/agents",
            "params": {"parentId": "_replace"},
            "headers": {
                "Content-Type": "application/json",
                "Accept": "application/json",
                "X-Auth": "_replace",
            },
        },
        "1302": {
            "url_base": "https://hosting.glonasssoft.ru/api/v3",
            "api_cmd": "/vehicles/find",
            "params": {
                "parentId": "_replace id agents",
            },
            "headers": {
                "Content-Type": "application/json",
                "Accept": "*/*",
                "X-Auth": "_replace",
            },
        },
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
