"""5. Escribir una función que reciba una lista como parámetro y devuelva True si la lista
está ordenada en forma ascendente o False en caso contrario. Por ejemplo,
ordenada([1, 2, 3]) retorna True y ordenada(['b', 'a']) retorna False. Desarrollar
además un programa para verificar el comportamiento de la función."""


def ordenada(lista):
    ordenada = True
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            ordenada = False
            break
    return ordenada 
            
        

#Programa Principal
lista = [2400,789,1100,4069]

if ordenada(lista) == True:
    print("La lista esta ordenada en forma ascendente")
else:
    print("La lista no esta ordenada en forma ascendente")
