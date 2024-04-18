lista1 = input("Ingresa una lista de números separados por comas: ").split(",")
lista2 = input("Ingresa una lista de números separados por comas: ").split(",")
verdadero = input(
    '¿True si quieres los elementos comunes o False si quieres los elementos no comunes? ')


def true_or_not(lista1, lista2, verdadero):
    lista1 = set(lista1)
    lista2 = set(lista2)
    if verdadero == "True":
        print(f'Los elementos comunes son: {lista1.intersection(lista2)}')
    else:
        print(f'Los elementos no comunes son: {lista1.difference(lista2)}')


true_or_not(lista1, lista2, verdadero)
