from asyncio.log import logger
import logging

# Creamos nuestro logger personalizado
logger = logging.getLogger(__name__)

# Seteamos el nivel de severidad
logger.setLevel(logging.DEBUG)

# Creamos el handler
handler1 = logging.FileHandler('app3.log')
handler2 = logging.StreamHandler()

# Ajustamos el nivel de severidad del handler
handler1.setLevel(logging.CRITICAL)
handler2.setLevel(logging.CRITICAL)

# Ajustamos el formato
format1 = logging.Formatter(' %(asctime)s %(name)s - %(levelname)s - %(message)s ')
format2 = logging.Formatter(' %(name)s - %(levelname)s - %(message)s ')

# Le agregamos el formato al handler creado
handler1.setFormatter(format1)
handler2.setFormatter(format2)

# Agregamos el handler al logger
logger.addHandler(handler1)
logger.addHandler(handler2)

#Probamos el logger personalizado
logger.critical('Este es un mensaje critico')






