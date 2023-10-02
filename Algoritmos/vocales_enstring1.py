
def suma_vocales(string):
    vocales = 0
    for vowel in string:
            if vowel in "aeiouáéíóú":
                vocales += 1
    return vocales

string = "qporoaeieoeaova oaeorui qique"
print(f'Final: {suma_vocales(string)}')
