"""5. La raíz cuadrada de un número puede obtenerse mediante la función sqrt() del
módulo math. Escribir un programa que utilice esta función para calcular la raíz
cuadrada de un número cualquiera ingresado a través del teclado. El programa
debe utilizar manejo de excepciones para evitar errores si se ingresa un número
negativo."""

import math
from colorama import Back, init
init(autoreset = True)

def calcular_raiz(numero):
    resultado = math.sqrt(numero)
    return resultado
            
#-----------Programa Principal-------------
while True:
    try:
        numero = int(input("Por favor ingrese un numero:"))
        assert numero >= 0
        break
    except ValueError:
        print(Back.RED + "El dato ingresado no es un numero valido")
    except AssertionError:
        print(Back.RED + "Error! El numero ingresado es negativo")

print(calcular_raiz(numero))


