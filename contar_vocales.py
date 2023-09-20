
def suma_vocales(array_strings):
    vocales = 0
    for word in array_strings:
        for vowel in word:
            if vowel in "aeiou":
                vocales = vocales + 1
                print(vocales)
    return vocales


array = ["qporqique", "ioqwuewo", "qweurweiore"]
print(f'Final: {suma_vocales(array)}')
