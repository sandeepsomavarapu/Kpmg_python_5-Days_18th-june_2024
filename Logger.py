import logging 
logging.basicConfig(filename='myapplogs.log',level=logging.DEBUG,filemode="w") 
print('Logging Demo') 
logging.debug('Debug Information') 
logging.info('info Information') 
logging.warning('warning Information') 
logging.error('error Information') 
logging.critical('critical Information')