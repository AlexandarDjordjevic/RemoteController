import argparse
from service import Discover

def print_foo():
    print('Foo...')

def print_bar():
    print('Bar')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--all', action='store_true')
    parser.add_argument('--uuid', action='store', type=str)
    args = parser.parse_args()
    if args.all:
        stbs = Discover.all()
        for stb in stbs:
            print ("UUID: " + stb.uuid)
            print ("Location: " + stb.location)
    if args.uuid:
        stb = Discover.uuid(args.uuid)
        if stb:
            print ("UUID: " + stb.uuid)
            print ("Location: " + stb.location)
        else:
            print("Can't find device with UUID: " + args.uuid)  
