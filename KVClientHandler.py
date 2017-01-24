import glob
import sys
import socket

sys.path.insert(0,'gen-py')
sys.path.insert(0,glob.glob('thrift/lib/py/build/lib*')[0])


from KVServer import KVInterface
from KVServer.ttypes import KVMessage, KVException

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

class KVClientHandler():
    port = 9000
    host = 'localhost'
    __label = "Key-Value Store Client"
    client = None
    def __init__(self):
        print(self.__label)

    def input_port(self,port):
        if port.isdigit() == True:
            self.port = int(port)
            print("Client try to use port {}".format(self.port))
        else:
            print("Invalid port")
            sys.exit(0)

    def input_host(self,host):
        try:
            socket.inet_aton(host)
            socket_answer = True
        except:
            socket_answer = False

        if host == 'localhost':
            print("Client try to connect to {}".format(self.host))
        elif socket_answer:
            self.host = host
            print("Client try to connect to {}".format(self.host))
        else:
            print("Invalid host")
            sys.exit(0)

    def work(self):
        # Make socket
        self.transport = TSocket.TSocket(self.host,self.port)

        # Buffering is critical. Raw sockets are very slow
        self.transport = TTransport.TBufferedTransport(self.transport)

        # Wrap in a protocol
        self.protocol = TBinaryProtocol.TBinaryProtocol(self.transport)

        # Create a client to use the protocol encoder
        self.client = KVInterface.Client(self.protocol)

        # Connect!
        self.transport.open()

    def ping(self):
        self.client.ping()
        print("ping()")

    def exit(self):
        self.transport.close()
        print("Exit Client, Good Bye")
        sys.exit(0)


# client.ping()
#
# client.set_element('hola','python')
#
# client.list_elements()
