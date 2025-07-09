import sys
import pandas as pd
import re

sys.path.append('gen-py')

print(sys.path)

from thrif.dispatch.server.thrif.backend.DispatchBackend import *
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from params import presp
from database import crud
from my_logger import logger

from params import presp
import ssl
from thrift.transport import TSSLSocket

class EraData:

    def __init__(self):

        self.params = dict()
        self.params = presp()
        self.groups = list()
        self.elm = dict()
        self.data = list()

    def __conn(self):

        ssl_context = ssl.create_default_context()
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE

        url_base = self.params['15']['url_base']
        url_port = self.params['15']['url_port']
        login = self.params['15']['params']['login']
        pwd = self.params['15']['params']['pwd']
        long_session = self.params['15']['long_session']

        # Подключить сокет
        transport = TSSLSocket.TSSLSocket(url_base, url_port, ssl_context=ssl_context)
        transport = TTransport.TFramedTransport(transport)
        # Получить TBinaryProtocol
        protocol = TBinaryProtocol.TBinaryProtocol(transport)

        open = transport.open()
        # Создать клиента
        client = Client(protocol)
        # Подключить транспорт канала

        # Вызов функции без возвращаемого значения
        id = client.login(login, pwd, long_session)
        inf_u = client.getCurrentUser(id)
        #inf_g = client.getGroup(id, inf_u.parentGroupId)
        inf_o = client.getChildrenMonitoringObjects(id, inf_u.parentGroupId, True)

        ostr = list()
        #ostr = []
        i = 0
        for el in inf_o:
            if len(ostr) == 0:
                ostr = [el.name]

            ostr.append(el.name)

            inf_g = client.getGroup(id, el.parentGroupId)

            self.data.append({'uid': el.parentGroupId, 'unm': inf_g.title, 'onm': el.name,
                'IMEI': el.tracker.identifier, 'oid': el.id})
            i += 1

        self.groups = client.getChildrenGroups(id, inf_u.parentGroupId, True)

        # Закрываем канал транспорта
        transport.close()
        res = { 'objects': self.data,
                'companies': self.groups
        }

        return res['objects']

    def list_to_csv(self) -> None:
        """
        Формирует CSV файл из json Era, адаптирует под Ромину бд
        """
        data = self.__conn()
        for item in data:
            item["unm"] = re.sub("[^0-9a-zA-ZА-я-_]+", " ", item["unm"])
            item["onm"] = " " + re.sub("[^0-9a-zA-ZА-я-_]+", " ", item["onm"])
            item["uid"] = " " + item["uid"]
            item["oid"] = " " + item["oid"]

        df = pd.DataFrame(data)
        df =  df[['unm', 'uid', 'onm', 'oid']]
        df['Days Active'] = ' Да'
        df.insert(2, 'Monitoring System ID',' 15')
        df.columns = ['Учётка', 'ID Учётки', 'ID Системы', 'Имя объекта', 'ID Объекта', "Активность"]

        df.to_csv('era.csv', index=False)

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

        try:
            crud.add_objects(list_obj)
            logger.info("Объекты из Era закончили соединение с базой данных")
        except Exception as e:
            logger.error(f"В добавлении в базу данных объектов из Era возникла ошибка: {e}")

