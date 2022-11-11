# Ejercicio práctico - Unidad 3

import logging

logging.basicConfig(
level= logging.DEBUG,
filename='file.log',
filemode= 'w',                                          #Aquí también puede ser 'a' de "append".
datefmt= '%d - %b-%y %H:%M:%S',
format='%(asctime)s - %(levelname)s - %(message)s',
)


fruits = ['Frutilla','Melón','PERA',99.6,'NaranJA', 'mORa', 'NisPERo',99]




for i in fruits:
    try:
        logging.info(f'conversión exitosa : {i} ----> {i.lower()}')
    except:
        logging.error(f'conversión fallida : {i}')

fruits_minus = print(str(fruits).lower())