#medios_transporte = ['auto', 'avión', 'barco', 'bicicleta', 'ómnibus' ]

TRANSPORTS = ['auto', 'avión', 'barco', 'bicicleta', 'ómnibus']


def request_index() -> str:
    """This Function take no params. Request for an index and show if it
    is posible to get value in a list of transports.

    :return: String
    :type: String
    """

    try:
        index = int(input("Give an index number: "))
        return f"Value {TRANSPORTS[index]} in position {index}"
    except Exception as error:
        print(f'Error - {type(error)}')
        request_index()


if __name__ == "__main__":
    print(request_index())