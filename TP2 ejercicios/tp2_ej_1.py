"""1. Desarrollar cada una de las siguientes funciones y escribir un programa que permita
verificar su funcionamiento imprimiendo la lista luego de invocar a cada función:
a. Cargar una lista con números al azar de cuatro dígitos. La cantidad de elementos
también será un número al azar de dos dígitos.
b. Calcular y devolver la sumatoria de todos los elementos de la lista anterior.
c. Eliminar todas las apariciones de un valor en la lista anterior. El valor a eliminar
se ingresa desde el teclado y la función lo recibe como parámetro.
d. Determinar si el contenido de una lista cualquiera es capicúa, sin usar listas
auxiliares. Un ejemplo de lista capicúa es [50, 17, 91, 17, 50]."""

import random

def cargar_lista():
    lista = []
    cant_elementos = random.randint(00,99)
    for i in range(cant_elementos):
        lista.append(random.randint(0000,9999))
    return lista

def sumar_lista():
    total = 0
    for i in lista:
        total += i
    return total

def eliminar_valor(valor_a_eliminar):
    repeticiones = lista.count(valor_a_eliminar)
    for i in repeticiones:
        lista.remove(valor_a_eliminar)
    
    

#Programa Principal
cargar_lista()

        
        