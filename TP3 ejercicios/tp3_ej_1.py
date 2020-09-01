"""1. Desarrollar cada una de las siguientes funciones y escribir un programa que permita
verificar su funcionamiento, imprimiendo la matriz luego de invocar a cada función:
a. Cargar números enteros en una matriz de N x N, ingresando los datos desde
teclado.
b. Ordenar en forma ascendente cada una de las filas de la matriz.
c. Intercambiar dos filas, cuyos números se reciben como parámetro.
d. Intercambiar dos columnas dadas, cuyos números se reciben como parámetro.
e. Trasponer la matriz sobre si misma. (intercambiar cada elemento Aij por Aji)
f. Calcular el promedio de los elementos de una fila, cuyo número se recibe como
parámetro.
g. Calcular el porcentaje de elementos con valor impar en una columna, cuyo número
se recibe como parámetro.
h. Determinar si la matriz es simétrica con respecto a su diagonal principal.
i. Determinar si la matriz es simétrica con respecto a su diagonal secundaria.
j. Determinar qué columnas de la matriz son palíndromos (capicúas), devolviendo
una lista con los números de las mismas.
NOTA: El valor de N debe leerse por teclado. Las funciones deben servir cualquiera
sea el valor ingresado."""

def cargar_matriz():
    n = int(input("Por favor ingrese el numero de filas y columnas de la matriz:"))
    filas = n
    columnas = n
    matriz = []
    for f in range(filas):
        matriz.append( [0] * columnas)
        for c in range(columnas):
            n = int(input("Ingrese el numero a ingresar en [{}][{}]:".format(f + 1,c + 1)))
            matriz[f][c] = n
    return matriz

def imprimir_matriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            print("%3d" %matriz[f][c], end = "")
        print()

def ordenar_filas(matriz):
    for filas in matriz:
        filas.sort()

def intercambiar_filas(matriz):
    pos_1 = int(input("Por favor ingrese el numero de la primera fila:")) - 1
    pos_2 = int(input("Por favor ingrese el numero de la segunda fila:")) - 1
    aux = matriz[pos_1]
    matriz[pos_1] = matriz[pos_2]
    matriz[pos_2] = aux

def intercambiar_columnas(matriz):
    col_1 = int(input("Por favor ingrese el numero de una columna:")) - 1
    col_2 = int(input("Por favor ingrese el numero de la otra columna:")) - 1
    for filas in matriz:
        aux = filas[col_1]
        filas[col_1] = filas[col_2]
        filas[col_2] = aux

def trasponer_matriz(matriz):
    matriz_traspuesta = []
    n = len(matriz)
    for f in range(n):
        matriz_traspuesta.append( [0] * n)
    for f in range(len(matriz)):
        for c in range(len(matriz[0])):
            matriz_traspuesta[c][f] = matriz[f][c]
    return matriz_traspuesta
            

            
            
            

            


#---------------Programa Principal-------------------#
matriz = cargar_matriz()
imprimir_matriz(matriz)
"""ordenar_filas(matriz)
intercambiar_filas(matriz)
imprimir_matriz(matriz)
intercambiar_columnas(matriz)
imprimir_matriz(matriz)
"""
print("Matriz traspuesta:")
print("----------------------------------")
m_t = trasponer_matriz(matriz)
imprimir_matriz(m_t)


    
    
    
