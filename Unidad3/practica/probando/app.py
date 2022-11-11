import imp
import importlib


import logging

logging.basicConfig(
level= logging.DEBUG,
filename='app.log',
filemode= 'w',                                          #Aquí también puede ser 'a' de "append".
datefmt= '%d/%b/%y - %H:%M:%S',
format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)

logging.debug('mensaje debug')
logging.info('mensaje info')
logging.warning('mensaje warning')
logging.error('mensaje error')
logging.critical('mensaje critical')