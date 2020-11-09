"""1. Desarrollar una función para ingresar a través del teclado un número natural. La
función rechazará cualquier ingreso inválido de datos utilizando excepciones y
mostrará la razón exacta del error. Controlar que se ingrese un número, que ese
número sea entero y que sea mayor que 0. Devolver el valor ingresado cuando
éste sea correcto. Escribir también un programa que permita probar el correcto
funcionamiento de la misma."""

from colorama import Fore, Back


def validar_ingreso():
    try:
        numero = int(input("Por favor ingrese un numero natural:"))
        assert numero > 0 
    except AssertionError as mensaje:
        print (Back.RED + "Error!, el numero ingresado debe ser mayor a 0")
    except ValueError:
        print(Back.RED + "Error!, el dato ingresado debe ser un numero entero")


#---------Programa Principal----------
validar_ingreso()



