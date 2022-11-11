medios_transporte = ['auto', 'avión', 'barco', 'bicicleta', 'ómnibus' ]

def request():

    print('Hola! Ingrese el número del elemento que desea visualizar')

    num = input('Introduce el número: ')
    num = int(num)


    print('Usted eligió ', medios_transporte[num])

request()