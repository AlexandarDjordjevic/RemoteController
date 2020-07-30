
from stb import STB
from ssdpy import SSDPClient

class Discover:
    def all():
        srvcs = SSDPClient().m_search()
        clients = []
        for x in srvcs:
            client = STB(x['usn'][len('uuid:'):], x['location'], "")
            clients.append(client)
        return clients

    def uuid(uuid):
        srvcs = SSDPClient().m_search()
        for x in srvcs:
            if x['usn'][len('uuid:'):] == uuid:
                client = STB(x['usn'][len('uuid:'):], x['location'], "")
                return client
    
