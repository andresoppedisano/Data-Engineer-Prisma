from asyncio.log import logger
from cgitb import handler



import logging
from logging.handlers import TimedRotatingFileHandler
from re import S

import formatter

# Creamos el logger
logger = logging.getLogger('simple_logger')

# Establecemos el nivel de severidad
logger.setLevel(logging.DEBUG)

# Creamos un Timed Rotating File Handler y seteamos el nivel de severidad DEBUG
handler = TimedRotatingFileHandler('Time_Log_test.log', when='S', interval=2, backupCount=50)
handler.setLevel(logging.DEBUG)

# Creamos un objeto de formato
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Agregamos el objeto formato al Timed Rotating File Handler
handler.setFormatter(formatter)

# Agregamos el handler al logger
logger.addHandler(handler)

# Generamos los logs

for i in range(100):

    logger.debug('debug message {}'.format(i))
    
    logger.info('info message {}'.format(i))
    
    logger.warning('warning message {}'.format(i))
    
    logger.error('error message {}'.format(i))
    
    logger.critical('critical message {}'.format(i))

