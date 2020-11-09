"""2. Realizar una función que reciba como parámetros dos cadenas de caracteres conteniendo
números reales, sume ambos valores y devuelva el resultado como un
número real. Devolver -1 si alguna de las cadenas no contiene un número válido,
utilizando manejo de excepciones para detectar el error."""

from colorama import Fore, Back, init
init(autoreset = True)

def sumar (cadena1, cadena2):
    try:
        resultado = float(cadena1) + float(cadena2)
    except ValueError:
        print(Back.RED + "Error: Cadena invalida, debe contener numeros reales")
        resultado = -1
    else:
        return resultado

#----------Programa principal------------
cadena1 = input("Por favor ingrese un numero real:")
cadena2 = input("Por favor ingrese otro numero real:")
print( sumar (cadena1, cadena2))
