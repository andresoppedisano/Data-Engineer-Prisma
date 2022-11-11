from asyncore import read
from logging import exception
import sys


def windows_interaction():
    assert ('win32' in sys.platform), "Esta función solamente funciona en windows"
    print('Sistema operativo win32')


try:
    windows_interaction()

except AssertionError as error:
    print(error)

else:
    try:
        with open('file.log') as file:
            read_data = file.read()
            print(read_data)
    except FileNotFoundError as fnf_error:
        print(fnf_error)