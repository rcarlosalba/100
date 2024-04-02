import math
numeral = input("Ingresa un número: ")


def isNar(numeral):
    nar = []
    for n in numeral:
        n = int(n)
        nar.append(int(math.pow(n, len(numeral))))
        nar_sum = sum(nar)
    if nar_sum == int(numeral):
        print(f"{numeral} es un número narcisista.")
    else:
        print(f"{numeral} no es un número narcisista.")


isNar(numeral)
