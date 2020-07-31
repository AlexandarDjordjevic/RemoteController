import requests
from logs import log

class STB:
    def __init__(self, uuid, location, nt):
        self.location = location
        self.uuid = uuid
        self.mac_address = ""
        self.nt = nt

    def getDescription(self):
        response = requests.get(self.location)
        if response.status_code == 200:
            log.info("Successfuly fetched device description")
        else:
            log.error("Fail to fetch device description")