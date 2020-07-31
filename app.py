import sys
import argparse
from logs import log
from scanner import Scanner

if __name__ == '__main__':
    # parser = argparse.ArgumentParser()
    # parser.add_argument('-d','--discoverall', action='store_true', help="discover all devices on network")
    # parser.add_argument('-u','--uuid', action='store', type=str, help="discover device with specific UUID")
    # args = parser.parse_args()
    # if len(sys.argv)==1:
    #     parser.print_usage()
    #     sys.exit()
    # if args.discoverall:
    #     stbs = Discover.all()
    #     if stbs:
    #         for stb in stbs:
    #             log.info("UUID  " + stb.uuid)
    #             log.info("Location  " + stb.descriptor_location)
    #     else:
    #         log.info("There is no available devices!")
    # else:
    #     if args.uuid:
    #         stb = Discover.uuid(args.uuid)
    #         if stb:
    #            log.info("UUID  " + stb.uuid)
    #            log.info("Location  " + stb.descriptor_location)
    #         else:
    #            log.error("Can't find device with UUID " + args.uuid)
    scanner = Scanner("0.0.0.0")
    scanner.listen()
    log.info('Type quit to quit :)')
    while True:
        nb = input()
        if nb == 'quit':
            log.info("Goodbye!")
            break
    scanner.stop()    
    scanner.join()

