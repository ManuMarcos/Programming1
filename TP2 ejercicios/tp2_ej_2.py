"""2. Escribir funciones para:
a. Generar una lista de 50 números aleatorios del 1 al 100.
b. Recibir una lista como parámetro y devolver True si la misma contiene algún
elemento repetido. La función no debe modificar la lista.
c. Recibir una lista como parámetro y devolver una nueva lista con los elementos
únicos de la lista original, sin importar el orden.
Combinar estas tres funciones en un mismo programa."""

import random

def generar_lista_aleatoria():
    lista = []
    for i in range(10):
        num_random = random.randint(1,100)
        lista.append(num_random)
    return lista
        
def elemento_repetido(lista):
    repetido = False
    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j]:
                repetido = True
    return repetido
                
def generar_lista_unica(lista):
    lista_unica = []
    for i in lista:
        if i not in lista_unica:
            lista_unica.append(i)
    return lista_unica

#Programa Principal
lista_aleatoria = generar_lista_aleatoria()
print(lista_aleatoria)

if elemento_repetido(lista_aleatoria) ==  True:
    print("En la lista hay algun elemento repetido")
else:
    print("En la lista no hay ningun elemento repetido")

print("Lista unica:",generar_lista_unica(lista_aleatoria))
    
        
        
        
    
    