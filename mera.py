import sys
import pandas as pd
import re
import typing

from thrif.dispatch.server.thrif.backend.DispatchBackend import *
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from database import crud
from my_logger import logger
import config

class EraData:


    def get_data(self):

        objects = []

        # Подключить сокет
        transport = TSocket.TSocket(str(config.ERA_HOST), 19990)
        transport = TTransport.TFramedTransport(transport)
        # Получить TBinaryProtocol
        protocol = TBinaryProtocol.TBinaryProtocol(transport)

        open = transport.open()
        # Создать клиента
        client = Client(protocol)

        # Вызов функции без возвращаемого значения
        session_id = client.login(
                config.ERA_LOGIN, 
                config.ERA_PASSWORD,
                True)
        inf_user = client.getCurrentUser(session_id)
        inf_objects = client.getChildrenMonitoringObjects(
                session_id, 
                inf_user.parentGroupId,
                True)

        ostr = list()
        i = 0
        for el in inf_objects:
            if len(ostr) == 0:
                ostr = [el.name]

            ostr.append(el.name)

            inf_groups = client.getGroup(
                    session_id, 
                    el.parentGroupId)

            objects.append({
                'uid': el.parentGroupId, 
                'unm': inf_groups.title, 
                'onm': el.name,
                'IMEI': el.tracker.identifier, 
                'oid': el.id})
            i += 1

        # Закрываем канал транспорта
        transport.close()


        for item in objects:
            item["unm"] = re.sub("[^0-9a-zA-ZА-я-_]+", " ", item["unm"])
            item["onm"] = " " + re.sub("[^0-9a-zA-ZА-я-_]+", " ", item["onm"])
            item["uid"] = " " + item["uid"]
            item["oid"] = " " + item["oid"]

        return objects

    @staticmethod
    def data_to_csv(data: typing.List) -> None:
        """
        Формирует CSV файл из json Era, адаптирует под Ромину бд
        """
        df = pd.DataFrame(data)
        df =  df[['unm', 'uid', 'onm', 'oid']]
        df['Days Active'] = ' Да'
        df.insert(2, 'Monitoring System ID',' 15')
        df.columns = ['Учётка', 'ID Учётки', 'ID Системы', 'Имя объекта', 'ID Объекта', "Активность"]

        df.to_csv('era.csv', index=False)

    @staticmethod
    def add_to_db(data: typing.List) -> None:
        list_obj = []
        for i in data:
            list_obj.append(
                    [
                        str(i["unm"]),
                        i["uid"],
                        "15",
                        i["onm"],
                        i["oid"],
                        " Да",
                    ]
                    )

        crud.add_objects(list_obj)

    def __str__(self) -> str:
        return str("era")

