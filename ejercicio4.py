def calcular_la_multiplicacion(numero1, numero2):
    if numero2 == 0:
        return 0
    else:
        return numero1 + calcular_la_multiplicacion(numero1, numero2 - 1)
resultado = calcular_la_multiplicacion(4, 3)
print(resultado)