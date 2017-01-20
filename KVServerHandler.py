import glob
import sys

sys.path.append('gen-py')
sys.path.insert(0,glob.glob('thrift/lib/py/build/lib*')[0])

from KVServer import KVInterface
from KVServer.ttypes import KVMessage, KVException, KVServer

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer


class KVServerHandler:
    def __init__(self):
        self.collection = KVServer([])

    def ping(self):
        print('ping()')

    def del_element(self):
        pass

    def set_element(self, key, value):
        print "key:{},value:{}".format(key,value)
        new_element = KVMessage({key:value})
        self.collection.elements.append(new_element)
        return new_element

    def get_element(self):
        pass

    def list_elements(self):
        key_list = []
        for element in self.collection.elements:
            value = element.value.keys()[0]
            key_list.append(value)
        return key_list



if __name__ == '__main__':
    handler = KVServerHandler()
    processor = KVInterface.Processor(handler)
    transport = TSocket.TServerSocket(port=8000)
    tfactory = TTransport.TBufferedTransportFactory()

    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

    print('Starting the server...')
    server.serve()
    print('done.')
