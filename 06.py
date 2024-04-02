numeral = int(input('Ingresa un número: '))

resultado = 1


def factorial(numeral):
    if numeral == 0:
        return 1
    else:
        return numeral * factorial(numeral-1)


print(f'El factorial de {numeral} es {factorial(numeral)}')
