from __future__ import division


def get_numbers(msj):
    print(msj)
    a = float(input())

    print('Ingresa el siguiente número:')
    
    b = float(input())

    division(a , b)


def division(a, b):
    try:
        resultado = a/b
        print('La división es: ', resultado)
    except ZeroDivisionError:
        get_numbers('--->No se puede dividir por cero. Ingresá los números nuevamente.')


get_numbers('Ingresa el primer número:')
