
def total_gastado_subte(cant_viajes):
    valor_pasaje = 19
    if cant_viajes <= 20:
        return valor_pasaje * cant_viajes
    elif cant_viajes <= 30:
        return (valor_pasaje - (valor_pasaje * 0.2)) * cant_viajes
    elif cant_viajes <= 40:
        return (valor_pasaje - (valor_pasaje * 0.3)) * cant_viajes
    else:
        return (valor_pasaje - (valor_pasaje * 0.4)) * cant_viajes

#Programa Principal
cant_viajes = int(input("Por favor ingrese la cantidad de viajes realizados en el mes:"))

print("Total gastado en viajes:", total_gastado_subte(cant_viajes))

        
