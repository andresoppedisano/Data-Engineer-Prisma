import logging
from sqlite3 import Row
from turtle import st
import lowermodule

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(name)s %(levelname)s:%(message)s', datefmt="%Y-%m-%dT%H:%M:%S%z")
logger = logging.getLogger(__name__)

def record_word_count(myfile):
    logger.info("iniciando la funcion")
    try:
        word_count = lowermodule.word_count(myfile)
        with open('wordcountarchive.csv', 'a') as file:
            row = str(myfile) + ',' + str(word_count)
            file.write(row + '\n')
    except:
        logger.warning("no se pudo escribir el archivo %s en el destino", myfile)
    finally:
        logger.debug("la función está hecha para el archivo %s", myfile)

def main():
    record_word_count('texto_prueba.txt')

if __name__ == '__main__':
    main()