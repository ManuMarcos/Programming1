"""4. Todo programa Python es susceptible de ser interrumpido mediante la pulsación de
las teclas Ctrl-C, lo que genera una excepción del tipo KeyboardInterrupt. Realizar
un programa para imprimir los números enteros entre 1 y 100000, y que solicite
confirmación al usuario antes de detenerse cuando se presione Ctrl-C."""

def imprimir_numeros():
    contador = 1
    while True:
        try:
            print(contador)
            contador += 1
        except KeyboardInterrupt:
            print()
            detener = input("Desea detener la ejecucion? (s/n):")
            if detener == "s":
                break
            else:
                pass


#----------Programa Principal--------------
imprimir_numeros()

        