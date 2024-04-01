decimal = int(input("Introduce un número decimal: "))


def convertir_a_binario(decimal):
    binario = ""
    while decimal // 2 != 0:
        binario += str(decimal % 2)
        decimal = decimal // 2

    print((binario + str(decimal))[::-1])


convertir_a_binario(decimal)
