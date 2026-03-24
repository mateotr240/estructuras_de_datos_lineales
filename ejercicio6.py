def suma_primeros_pares(n):
    if n < 2:
        return 0
    if n % 2 == 0:
        return n + suma_primeros_pares(n - 2)
    else:
        return suma_primeros_pares(n - 1)
resultado = suma_primeros_pares(5)
print(resultado)