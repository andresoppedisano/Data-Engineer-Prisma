a = 10
b = 0

try:
    a/b
except ZeroDivisionError:
    print('No se puede dividir por cero')