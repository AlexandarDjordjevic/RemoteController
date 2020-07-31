import requests
from logs import log

class STB:
    def __init__(self, uuid, location):
        self.location = location
        self.uuid = uuid
        self.mac_address = ""

    def getDescription(self):
        response = requests.get(self.descriptor_location)
        if response.status_code == 200:
            log.info("Successfuly fetched device description")
        else:
            log.error("Fail to fetch device description")