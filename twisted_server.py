#!/usr/bin/env python3

# pip install twisted
import logging

from twisted.internet import reactor
from twisted.internet import protocol
from twisted.internet import endpoints

logging.basicConfig(level=logging.DEBUG,
                    filename='twisted_server.log',
                    filemode='w',
                    format='%(asctime)s - %(levelname)s - %(message)s')


class ProcessClient(protocol.Protocol):

    def __init__(self, server):
        self.server = server

    def connectionMade(self):
        logging.info('Client connected...')
        self.server.concurrentClientCount += 1

    def connectionLost(self, reason=protocol.connectionDone):
        self.server.concurrentClientCount -= 1

    def dataReceived(self, data: str):
        data = data.strip()
        logging.info(f'Received data: {data}')
        self.transport.write(data)


class Server(protocol.Factory):
    commands = ('init', 'send', 'get', 'close')

    def __init__(self):
        self.concurrentClientCount = 0
        self.database = {}

    def buildProtocol(self, addr):
        return ProcessClient(self)


if __name__ == '__main__':
    logging.info('Server started...')
    server = endpoints.serverFromString(reactor, 'tcp:8888')
    server.listen(Server())
    reactor.run()
