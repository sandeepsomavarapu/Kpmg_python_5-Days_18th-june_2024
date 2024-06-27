import logging 
#format='%(levelname)s
#format='%(levelname)s:%(message)s'

logging.basicConfig(filename='myapplogs1.txt',level=logging.DEBUG,filemode="a",format='%(asctime)s:%(levelname)s:%(message)s') 
print('Logging Demo') 
logging.debug('Debug Information') 
logging.info('info Information') 
logging.warning('warning Information') 
logging.error('error Information') 
logging.critical('critical Information')