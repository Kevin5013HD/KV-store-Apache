import glob
import sys

sys.path.insert(0,'gen-py')
sys.path.insert(0,glob.glob('thrift/lib/py/build/lib*')[0])

from KVServer import KVInterface
from KVServer.ttypes import KVMessage, KVException, KVCollection

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer


class KVServerHandler:
    def __init__(self):
        self.collection = KVCollection([])

    def ping(self):
        print('ping()')

    def del_element(self,key):
	try:
            for kvmessage in self.collection.elements:
                if kvmessage.value.has_key(key):
                    self.collection.elements.remove(kvmessage)
                    return True
        except Except:
            # raise KVException("Something wrong :(  ")
            return False


    def set_element(self, key, value):
        print "key:{},value:{}".format(key,value)
        new_element = KVMessage({key:value})
        self.collection.elements.append(new_element)
        return new_element

    def get_element(self,key):
        try:
            for kvmessage in self.collection.elements:
                if kvmessage.value.has_key(key):
                    return kvmessage.value.get(key)
        except Except:
            raise KVException(why="Element not found :(")


    def list_elements(self):
        key_list = []
        for element in self.collection.elements:
            value = element.value.keys()[0]
            key_list.append(value)
        return key_list
