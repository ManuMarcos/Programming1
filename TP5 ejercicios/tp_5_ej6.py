"""6. El método index permite buscar un elemento dentro de una lista, devolviendo la
posición que éste ocupa. Sin embargo, si el elemento no pertenece a la lista se
produce una excepción de tipo ValueError. Desarrollar un programa que cargue
una lista con números enteros ingresados a través del teclado (terminando con -1)
y permita que el usuario ingrese el valor de algunos elementos para visualizar la
posición que ocupan, utilizando el método index. Si el número no pertenece a la
lista se imprimirá un mensaje de error y se solicitará otro para buscar. Abortar el
proceso al tercer error detectado. No utilizar el operador in durante la búsqueda."""

from colorama import init, Fore, Back
init(autoreset = True)

def cargar_lista():
    lista = []
    numero = int(input("Ingrese un numero:"))
    while numero != -1:
        lista.append(numero)
        numero = int(input("Ingrese un numero(-1 para terminar):"))
    return lista


def buscar_numero(lista):
    contador = 0
    while contador < 3:
        try:
            numero_a_buscar = int(input("Ingrese el numero que quiere buscar:"))
            pos = lista.index(numero_a_buscar)
            print("Numero buscado:{} , Posicion:{}".format(numero_a_buscar,pos))
        except ValueError:
            print(Back.RED + "El numero ingresado no se encuentra en la lista")
            contador += 1
    print(Back.WHITE + Fore.RED + "Alcanzaste 3 errrores por lo tanto se freno la ejecucion")

        
            
#--------------Programa Principal-----------------
lista = cargar_lista()
buscar_numero(lista)

            