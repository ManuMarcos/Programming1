"""3. Desarrollar una función que devuelva una cadena de caracteres con el nombre del
mes cuyo número se recibe como parámetro. Los nombres de los meses deberán
obtenerse de una lista de cadenas de caracteres inicializada dentro de la función.
Devolver una cadena vacía si el número de mes es inválido. La detección de meses
inválidos deberá realizarse a través de excepciones."""

from colorama import Fore, Back

def nombre_mes (numero):
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre",
             "Noviembre", "Diciembre"]
    try:
        assert 0 < numero <= 12
    except AssertionError:
        print(Back.RED + "Error!, el numero de mes ingresado es incorrecto (0 < meses <= 12)")
        return ""
    else:
        return meses[numero - 1]

#-----------Programa Principal------------------
while True:
    try:
        numero = int(input("Por favor ingrese el numero del mes:"))
        break   
    except ValueError:
        print("Error!, debe ingresar un numero")
print(nombre_mes(numero))