from cgitb import handler
from distutils.log import debug
import logging
from logging.handlers import RotatingFileHandler



# Creamos el logger
logger = logging.getLogger('simple_logger')

# Establecemos el nivel de severidad
logger.setLevel(logging.DEBUG)

# Creamos un RotatingFileHandler y seteamos el nivel de severidad en Debug
handler = RotatingFileHandler('my_log.log', maxBytes=100, backupCount=200)
handler.setLevel(logging.DEBUG)

# Creamos un objeto de formato
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Agregamos el objeto formato al RotatingFileHandler
handler.setFormatter(formatter)

# Agregamos el handler al logger
logger.addHandler(handler)

# Generamos los logs
for i in range(500):

    logger.debug('debug message {}'.format(i))
    
    logger.info('info message {}'.format(i))
    
    logger.warning('warning message {}'.format(i))
    
    logger.error('error message {}'.format(i))
    
    logger.critical('critical message {}'.format(i))

