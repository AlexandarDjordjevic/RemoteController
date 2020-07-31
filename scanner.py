
from stb import STB
from logs import log
#from ssdpy import SSDPClient
from socket import *
from threading import *
try:
    from http_parser.parser import HttpParser
except ImportError:
    from http_parser.pyparser import HttpParser

class Scanner(Thread):
    def __init__(self, ip_address):
        Thread.__init__(self)
        self.ip_address = ip_address
        self.listener = socket(AF_INET, SOCK_DGRAM, 0)
        self.listener.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.listener.bind((self.ip_address, 1900))
        self.listener.setsockopt(IPPROTO_IP, IP_ADD_MEMBERSHIP, 
                        inet_aton('239.255.255.250') + inet_aton(self.ip_address))
        self.stbs = []
        self.mutex = Lock()
        self.running = False

    # def search():
    #     SSDPClient().m_search()    

    def run(self):
        while self.running:
            data, addr = self.listener.recvfrom(4096)
            http_pareser = HttpParser()
            http_pareser.execute(data, len(data))
            headers = http_pareser.get_headers()

            try:
                if headers['NTS'] == 'ssdp:alive' and headers['NT'] == 'urn:zenterio-net:service:X-CTC_RemotePairing:1':
                    stb = STB(uuid=headers['USN'][5:41], location=headers['LOCATION'], nt=headers['NT'])
                    self.mutex.acquire(1)
                    for x in self.stbs:
                        if x.uuid == stb.uuid:
                            break
                    else:
                        self.stbs.append(stb)
                        log.info('-------------------------------------------')
                        log.info("New STB detected!")
                        log.info("UUID: " + stb.uuid)
                        log.info("Location: " + stb.location)
                        log.info("NT: " + stb.nt)
                    self.mutex.release()
            except:
                pass
            

    def listen(self):
        self.running = True
        self.start()

    def stop(self):
        self.running = False
