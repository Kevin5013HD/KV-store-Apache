import sys
import glob

sys.path.append('gen-py')
sys.path.insert(0, glob.glob('thrift/lib/py/build/lib*')[0])

from KVServer import KVInterface
from KVServer.ttypes import KVMessage, KVException


from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

def main():
    # Make socket
    transport = TSocket.TSocket('localhost', 8000)

    # Buffering is critical. Raw sockets are very slow
    transport = TTransport.TBufferedTransport(transport)

    # Wrap in a protocol
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    # Create a client to use the protocol encoder
    client = KVInterface.Client(protocol)

    # Connect!
    transport.open()

    client.ping()

    client.set_element('hola','python')

    client.list_elements()

if __name__ == '__main__':
    try:
        main()
    except Thrift.TException as tx:
        print('%s' % tx.message)
