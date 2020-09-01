"""12.Resolver el siguiente problema, utilizando funciones:
Se desea llevar un registro de los socios que visitan un club cada día. Para ello, se
ingresa el número de socio de cinco dígitos hasta ingresar un cero como fin de carga.
Se solicita:
a. Informar para cada socio, cuántas veces ingresó al club (cada socio debe
aparecer una sola vez en el informe).
b. Solicitar un número de socio que se dio de baja del club y eliminar todos
sus ingresos. Mostrar los registros de entrada al club antes y después de
eliminarlo. Informar cuántos ingresos se eliminaron."""

def cargar_socios():
    r_ingreso = []
    nro_socio = int(input("Por favor ingrese el nro de socio:"))
    while nro_socio != 0:
        r_ingreso.append(nro_socio)
        nro_socio = int(input("Por favor ingrese el nro de socio:"))
    return r_ingreso

def planilla_ingresos(lista):
    lista_borrador = []
    for i in lista:
        if i not in lista_borrador:
            lista_borrador.append(i)
            print("Nro socio:", i, "| Cant ingresos:", lista.count(i))

def eliminar_socio(lista):
    nro_socio = int(input("Por favor ingrese el nro de socio que desea eliminar:"))
    ingresos_eliminados = 0
    while nro_socio not in lista:
        print("El nro ingresado no se encuentra en la lista")
        nro_socio = int(input("Por favor ingrese el nro de socio que desea eliminar:"))
    print("--------------------------------------------")
    print("Planilla de ingresos antes de eliminar socio")
    print("--------------------------------------------")
    planilla_ingresos(lista)
    while lista.count(nro_socio) > 0:
        lista.remove(nro_socio)
        ingresos_eliminados += 1
    print("----------------------------------------------")
    print("Planilla de ingresos despues de eliminar socio")
    print("----------------------------------------------")
    planilla_ingresos(lista)
    print("Cantidad de ingresos eliminados:", ingresos_eliminados)
            

    
#-------------Programa Principal------------------#
r_ingreso = cargar_socios()
print(r_ingreso)
planilla_ingresos(r_ingreso)
eliminar_socio(r_ingreso)




        