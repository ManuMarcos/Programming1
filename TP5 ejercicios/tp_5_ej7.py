"""7. Escribir un programa que juegue con el usuario a adivinar un número. El programa
debe generar un número al azar entre 1 y 500 y el usuario debe adivinarlo. Para
eso, cada vez que se introduce un valor se muestra un mensaje indicando si el número
que tiene que adivinar es mayor o menor que el ingresado. Cuando consiga
adivinarlo, se debe imprimir en pantalla la cantidad de intentos que le tomó hallar
el número. Si el usuario introduce algo que no sea un número se mostrará un
mensaje en pantalla y se lo contará como un intento más."""

import random
from colorama import init, Fore, Back
init(autoreset = True)

def adivinar_numero():
    numero_a_adivinar = random.randint(1,500)
    print(numero_a_adivinar)
    intentos = 0
    while True:
        try:
            numero_ingresado = int(input("Por favor ingrese un numero:"))
            assert 1 <= numero_ingresado <= 500
            if numero_ingresado > numero_a_adivinar:
                print("El numero a adivinar es menor al ingresado")
                intentos += 1
            elif numero_ingresado < numero_a_adivinar:
                print("El numero a adivinar es mayor al ingresado")
                intentos += 1
            else:
                intentos += 1
                print(Back.YELLOW + Fore.BLACK
                      + "Felicitaciones acertaste el numero!!, Numero de intentos:{}".format(intentos))
                break
        except ValueError:
            print(Back.RED + "El dato ingresado no es un numero")
            intentos += 1
        except AssertionError:
            print(Back.RED + "El numero ingresado debe estar entre 1 y 500")
            
            
#------------------Programa Principal---------------
adivinar_numero()
