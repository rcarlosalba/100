palabra = input("Introduce una palabra: ")


def volteando(texto):
    for i in range(len(texto)-1, -1, -1):
        print(texto[i], end="")


volteando(palabra)
