import sys
sys.path.append("..\\ThriftPython\Thrift")
sys.path.append('gen-py')


#sys.path.append("..\\..\\gen-py")
#sys.path.append("\\")
#sys.path.append(".\\dispatch\\server\\thrift\\backend")
#sys.path.append("..\\..\\Thrift\\lib\\build\\lib.win-amd64-3.10\\thrift")
#sys.path.append("./Thrift")
#sys.path.append("./gen-py/dispatch/server/thrift/backend")

#from dispatch.server.thrift.backend.DispatchBackend import *

print(sys.path)


from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
from thrift.TRecursive import fix_spec

from thrift.transport.TSSLSocket import TSSLSocket

#from backend import dispatch\server\thrift\backend\DispatchBackend.py
from dispatch.server.thrift.backend.DispatchBackend import *
#from  dispatch.server.thrift.backend import DispatchBackend
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

def checkIfDuplicates_1(listOfElems):
    ''' Check if given list contains any duplicates '''
    if len(listOfElems) == len(set(listOfElems)):
        return False
    else:
        return True

try:
    # Подключить сокет
    transport = TSocket.TSocket('monitoring.aoglonass.ru', 19990)
    #transport = TSSLSocket('monitoring.aoglonass.ru', 19991, validate=True, ca_certs=ca_cert)
         # Получить транспорт
    #transport = TTransport.TBufferedTransport(transport)    
    transport = TTransport.TFramedTransport(transport)
        # Получить TBinaryProtocol
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    open = transport.open()
    print(open)
    print(protocol)
        # Создать клиента
    client = Client(protocol)
        # Подключить транспорт канала
    #open = transport.open()
   
        # Вызов функции без возвращаемого значения
    # try:         
    id = client.login('santels', 'GfR736', True)
    inf_u = client.getCurrentUser(id)
    print(type(inf_u))
    inf_g = client.getGroup(id, inf_u.parentGroupId)
    inf_o = client.getChildrenMonitoringObjects(id, inf_u.parentGroupId, True)
    
    print(inf_u, '\n \n', inf_o)
    ostr = list()
    ostr = ['']
    i = 0    
    for el in inf_o:
        inf_g = client.getGroup(id, el.parentGroupId)
        i += 1
        ostr.append(el.name)
        print('\n \n', el, '\n \n', inf_g, '\n \n', i)
        if (el.name == 'Navtelecom СИГНАЛ S-2651'):
            break

    if checkIfDuplicates_1(ostr):
        print('Find Dublicates', len(ostr))
    else:
        print('Don\'t find Dublicates', len(ostr))

    for el in ostr:
        print(el)
    # except:
        # Вызов функции с возвращаемым значением   
    print('\n id:', id)
        # Закрываем канал транспорта
    transport.close()
except BadRequest:
    print(message)
except Busy:
    print(message)
except InternalServerError:
    print(message)
except AccessDenied:
    print(message)
except UserLicenseExpired:
    print(message)
except TrialIsNotActivated:
    print(message)
except LoginFailed:
    print(message)       
except Thrift.TException as e:    
    print('%s' % (e.message))
    pass

