import logging

logging.basicConfig(
level= logging.DEBUG,
filename='app2.log',
filemode= 'w',                                          #Aquí también puede ser 'a' de "append".
datefmt= '%d-%b-%y  %H:%M:%S',
format='%(asctime)s - %(levelname)s - %(levelno)s - %(message)s',
)

a = 5
b = 0

try:
    a/b
except Exception as e:
    logging.error('¡Encontramos una excepcion!', exc_info= True)