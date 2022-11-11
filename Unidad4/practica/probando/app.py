from asyncio.log import logger
import logging
import logging.config

logging.config.fileConfig(fname='custom.conf', disable_existing_loggers=False)

# Obtener el logger especificado en el archivo
logging = logging.getLogger(__name__)

logger.debug('Este es un mensaje debug')
