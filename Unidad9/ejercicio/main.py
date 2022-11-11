medios_transporte = ['auto', 'avión', 'barco', 'bicicleta', 'ómnibus']


def solicitar_numero():
    """Esta función no recibe parámetros. Solicita un índice y muestra si es posible obtener un valor en una lista de transportes.

    :return: Medio de transporte.
    :rtype: string
    """

    try:
        num = input('Ingrese el número del elemento que desea visualizar: ')
        num = int(num)
        print('Usted eligió:', medios_transporte[num])

    except Exception:
        print('Valor incorrecto. Intente nuevamente...')
        return solicitar_numero()


solicitar_numero()
