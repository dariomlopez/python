
def factorial(num):
    def segunda_llamada(result):
        result = num * (num - 1)
        return result


num = 5
print(f'Final: {factorial(num)}')
