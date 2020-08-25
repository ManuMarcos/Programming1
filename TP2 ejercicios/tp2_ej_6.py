"""Escribir una función que reciba una lista de números enteros como parámetro y la
normalice, es decir que todos sus elementos deben sumar 1.0, respetando las proporciones
relativas que cada elemento tiene en la lista original. Desarrollar también
un programa que permita verificar el comportamiento de la función. Por ejemplo,
normalizar([1, 1, 2]) debe devolver [0.25, 0.25, 0.50]."""

def normalizar(lista):
    valor_unidad = 1 / sum(lista)
    for i in range(len(lista)):
        lista[i] = valor_unidad * lista[i]
    print("Suma de la lista normalizada",sum(lista))
    return lista


#Programa Principal
lista = [2,3,1,2,3,2]
print(normalizar(lista))
