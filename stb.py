import requests
from logs import log

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
class STB:
    def __init__(self, uuid, location, mac_address):
        self.descriptor_location = location
        self.uuid = uuid
        self.mac_address = mac_address

    def getDescription(self):
        response = requests.get(self.descriptor_location)
        if response.status_code == 200:
            log.info("Successfuly fetched device description")
        else:
            log.error("Fail to fetch device description")