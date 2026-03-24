
def suma_primeros_n_numeros(numero1, lista=[]): 
    if  numero1 <= 0:
        return 0
    else:
        return lista[numero1 - 1] + suma_primeros_n_numeros(numero1 - 1, lista)
resultado = suma_primeros_n_numeros(3, [2,4,6,8,10,12])
print(resultado)