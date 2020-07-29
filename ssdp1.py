from ssdpy import SSDPServer

server = SSDPServer(usn="uuid:12345", location="192.168.0.2")
server.serve_forever()