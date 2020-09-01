"""3. Desarrollar un programa para rellenar una matriz de N x N con números enteros al
azar comprendidos en el intervalo [0,N2), de tal forma que ningún número se repita.
Imprimir la matriz por pantalla."""

import random

def cargar_matriz():
    n = int(input("Por favor ingrese el numero de filas y columnas:"))
    numeros_cargados = []
    matriz = []
    for f in range(n):
        matriz.append([])
        for c in range(n):
            numero_random = random.randint(0, (n * n) - 1)
            while numero_random in numeros_cargados:
                numero_random = random.randint(0, (n * n) - 1)
            numeros_cargados.append(numero_random)
            matriz[f].append(numero_random)
    return matriz

def imprimir_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print("%3d" %elemento, end = "")
        print()
    



#-----------------Programa Principal------------------#
matriz = cargar_matriz()
imprimir_matriz(matriz)

