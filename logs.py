import logging

logging.basicConfig(format="[%(filename)s:%(lineno)d] %(levelname)s: %(message)s",  
                    datefmt='%Y-%m-%d:%H:%M:%S', 
                    level=logging.DEBUG)

log = logging.getLogger(__name__)
