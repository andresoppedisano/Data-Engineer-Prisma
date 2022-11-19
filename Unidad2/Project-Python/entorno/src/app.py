from decouple import config                        #importamos desde Decouple, un objeto llamado “config”.
print(config('POSTGRESQL_HOST'))                   #imprimimos cada uno de los valores de las 4 propiedades indicadas para el objeto config.
print(config('POSTGRESQL_PORT'))
print(config('POSTGRESQL_USER'))
print(config('POSTGRESQL_PWD'))



#Ahora vamos a imprimir los valores de Host y Port por medio de Placeholders.

#print('Host: {HOST} - Puerto: {PORT}'.format(HOST=config('POSTGRESQL_HOST'), PORT=config('POSTGRESQL_PORT')))

#ejecutamos la app con el siguiente código: ' python .\SRC\app.py '



#Comento el código anterior de la aplicación Python desarrollada
#Procedo a mostrar las variables de entorno por pantalla utilizado dotenv.

import os
from dotenv import load_dotenv, find_dotenv
load_dotenv (find_dotenv())
print(os.getenv('POSTGRESQL_HOST'))
print(os.getenv('POSTGRESQL_PORT'))
print(os.getenv('POSTGRESQL_USER'))
print(os.getenv('POSTGRESQL_PWD'))