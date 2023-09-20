def suma_pares(array_numeros):
    resultado = 0
    for number in array_numeros:
        if number % 2 == 0:
            resultado = resultado + number
            print(resultado)
    return resultado


array = [5, 44, 9, 12, 3, 33, 99, 87, 48, 32]
print(suma_pares(array))
