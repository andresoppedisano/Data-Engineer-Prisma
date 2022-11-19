# Ejercicio práctico - Unidad 6


def contador():

    # Inicializamos la lista con sus respectivos valores
    lista_inicial = ['perro', 'elefante', 'dragón']

    # Se cuenta la cantidad de caracteres de cada palabra
    caracteres0 = len(lista_inicial[0])
    caracteres1 = len(lista_inicial[1])
    caracteres2 = len(lista_inicial[2])

    # Formulamos la lista retorno
    lista_retorno = [caracteres0, caracteres1, caracteres2]

    # Se imprime en pantalla dicha lista
    print(lista_retorno)


contador()
