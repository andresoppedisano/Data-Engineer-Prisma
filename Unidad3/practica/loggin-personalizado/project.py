from asyncio.log import logger
import logging


#Creamos nuestro logger personalizado
logger = logging.getLogger(__name__)

#Ajustamos el nivel de severidad
logger.setLevel(logging.DEBUG)

#Creamos los handlers
c_handler = logging.StreamHandler()                     #Muesta el handler por consola
f_handler = logging.FileHandler('app.log')              #Crea un nuevo archivo .log y muestra el handler dentro

#Ajustamos el nivel de severidad de los handlers
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.ERROR)

#Ajustamos el formato y lo agregamos a cada handler
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

#Agregamos los handlers al logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)

#Probamos el logger personalizado
logger.warning('Este es un mensaje de warning')
logger.error('Este es un mensaje de error')