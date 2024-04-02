oracion = input("Ingrese una oración: ")
oracion = oracion.split()


def make_title(oracion):
    for w in oracion:
        w = w[0].upper() + w[1:]
        print(w, end=" ")
    print()


make_title(oracion)
