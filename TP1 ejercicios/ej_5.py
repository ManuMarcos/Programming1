
def imprimir_asteriscos_1(cant_filas):
    for i in range(0,cant_filas):
        print("**********")

def imprimir_asteriscos_2(cant_filas):
    patron = "**"
    contador = 1
    for i in range(0,cant_filas):
        print(patron * contador)
        contador +=1

        
#Programa Principal 
cant_filas = int(input("Por favor ingrese la cantidad de filas:"))
imprimir_asteriscos_1(cant_filas)
print("--------------------------------------------------------")
imprimir_asteriscos_2(cant_filas)

