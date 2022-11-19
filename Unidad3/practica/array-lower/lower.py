# Ejercicio práctico - Unidad 3


import logging

# Configuramos el logging
logging.basicConfig(
level= logging.DEBUG,
filename='result.log',      # Creamos el archivo .log para guardar los registros
filemode= 'a',
datefmt= '%d - %b-%y %H:%M:%S',
format='%(asctime)s - %(levelname)s - %(message)s',
)

# Se requiere convertir la siguiente lista
fruits = ['Frutilla','Melón','PERA',99.6,'NaranJA', 'mORa', 'NisPERo',99]



# Realizar conversión
for i in fruits:
    try:
        logging.info(f'conversión exitosa : {i} ----> {i.lower()}')
    except:
        logging.error(f'conversión fallida : {i}')

fruits_minus = print(str(fruits).lower())