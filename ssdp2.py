from ssdpy import SSDPServer

server = SSDPServer(usn="uuid:54321", location="192.168.0.1")
server.serve_forever()