
def vuelto_cajero(total_compra, dinero_recibido):
    billetes = [500,0,100,0,50,0,20,0,10,0,5,0,1,0]
    if dinero_recibido < total_compra:
        print("El dinero recibido es insuficiente!!")
    else:
        vuelto = dinero_recibido - total_compra
        aux = vuelto
        i , j = 1, 0
        fin = False
        while fin == False:
            billetes[i] = aux // billetes[j]
            aux -= billetes[i] * billetes[j]
            i += 2
            j += 2
            if aux == 0:
                fin = True
    return billetes, vuelto

def imprimir(lista, vuelto):
    print("----------------------------------------------------------------------")
    print("El vuelto es de",vuelto,"pesos distribuido en los siguientes billetes:")
    for i in range(0, len(lista) - 1, 2):
        print("Billetes de",lista[i],":",lista[i+1])
    print("----------------------------------------------------------------------")
        
#Programa Principal        
total_compra = int(input("Por favor ingrese el total de la compra:"))
dinero_recibido = int(input("Por favor ingrese el dinero recibido:"))

billetes,vuelto = vuelto_cajero(total_compra, dinero_recibido)
imprimir(billetes, vuelto)


            
        
        
        
        
        
        

