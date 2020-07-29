import sys
import argparse
from service import Discover

def print_foo():
    print('Foo...')

def print_bar():
    print('Bar')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d','--discoverall', action='store_true', help="discover all devices on network")
    parser.add_argument('-u','--uuid', action='store', type=str, help="discover device with specific UUID")
    args = parser.parse_args()
    if len(sys.argv)==1:
        parser.print_usage()
        sys.exit()
    if args.discoverall:
        stbs = Discover.all()
        for stb in stbs:
            print ("UUID: " + stb.uuid)
            print ("Location: " + stb.location)
    else:
        if args.uuid:
            stb = Discover.uuid(args.uuid)
            if stb:
                print ("UUID: " + stb.uuid)
                print ("Location: " + stb.location)
            else:
                print("Can't find device with UUID: " + args.uuid)

