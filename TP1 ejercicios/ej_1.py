def obtener_max( a, b, c):
    if a > b:
        if a > c:
            return a
    elif b > a:
        if b > c:
            return b
    elif c > a:
        if c > b:
            return c
    else:
        return -1
    
a = int(input("Por favor ingrese el primer numero:"))
b = int(input("Por favor ingrese el segundo numero:"))
c = int(input("Por favor ingrese el tercer numero:"))

resultado = obtener_max(a,b,c)

if resultado != -1:
    print("El mayor valor hallado es:",resultado)
else:
    print("Error, no existe un valor mayor estricto")
    

