import sys
from ssdpy import SSDPServer

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: " + sys.argv[0] + ' <UUID> <LOCATION>')
        exit()
    print ("Simulate device. UUID: {} Location: {}".format(sys.argv[1], sys.argv[2]))
    server = SSDPServer(usn="uuid:" + sys.argv[1], location=sys.argv[2])
    server.serve_forever()