"""
try:
    d = 2 + "Hola"
except Exception as exp:
    print('No se pudo realizar la operación debido a la excepción', type(exp))
"""

try:
    d = 10 / 5
except Exception as exp:
    print('No se pudo realizar la operación debido a la excepción', type(exp))
else:
    print('No ha ocurrido ninguna excepción.')
