import glob
import sys

sys.path.insert(0,'gen-py')
sys.path.insert(0,glob.glob('thrift/lib/py/build/lib*')[0])

from KVServer import KVInterface
from KVServer.ttypes import KVMessage, KVException
from KVClientHandler import KVClientHandler

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

class KVClient():
    client_handler = None

    def connect(self):
        self.client_handler = KVClientHandler()
        if len(sys.argv) == 1:
            print("Client try to connect to host:port by default: {}:{}".format(self.client_handler.host,self.client_handler.port))
        elif len(sys.argv) == 3:
            self.client_handler.input_host(sys.argv[1])
            self.client_handler.input_port(sys.argv[2])
        self.client_handler.work()

    def expr(self,command):
        if command == 'ping':
            self.client_handler.ping()
        elif command == 'exit':
            self.client_handler.exit()



if __name__ == '__main__':
    try:
        Client = KVClient()
        Client.connect()
        while True:
            try:
                command = raw_input('KVClient> ')
            except EOFError:
                break
            if not command:
                continue
            operation  = Client.expr(command)
    except Thrift.TException as tx:
        print("Error: Invalid Port or Host, please try again with the correct port or host\n{}".format(tx.message))
        sys.exit(0)
