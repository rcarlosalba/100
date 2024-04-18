print('Welcome to The Pizzeria')
print('------------------------')
print(' La base es la masa de la pizza, la salsa de tomate y el queso mozzarella.')
print(' Elige tus ingredientes favoritos para añadir a tu pizza.')
print(' Cuando hayas terminado, te diremos el precio de tu pizza.')
print('------------------------')
print('Ingredientes:')
print(' 1. Jamón')
print(' 2. Champiñones')
print(' 3. Pimientos')
print(' 4. Queso extra')
print(' 5. Aceitunas')
print(' 6. Pepperoni')
print(' 7. Salchichas')
print(' 8. Anchoas')
print(' 9. Pollo')
print(' 10. Carne de kebab')
print('------------------------')
print('Precios:')
print(' Jamón: 2 €')
print(' Champiñones: 1 €')
print(' Pimientos: 1 €')
print(' Queso extra: 1 €')
print(' Aceitunas: 1 €')
print(' Pepperoni: 2 €')
print(' Salchichas: 2 €')
print(' Anchoas: 3 €')
print(' Pollo: 3 €')
print(' Carne de kebab: 4 €')
print('------------------------')
print('Escribe "fin" para terminar de añadir ingredientes.')
print('------------------------')
total = 0
while True:
    ingredient = input('Elige un ingrediente: ')
    if ingredient == '1':
        total += 2
    elif ingredient == '2':
        total += 1
    elif ingredient == '3':
        total += 1
    elif ingredient == '4':
        total += 1
    elif ingredient == '5':
        total += 1
    elif ingredient == '6':
        total += 2
    elif ingredient == '7':
        total += 2
    elif ingredient == '8':
        total += 3
    elif ingredient == '9':
        total += 3
    elif ingredient == '10':
        total += 4
    elif ingredient == 'fin':
        break
    else:
        print('Ingrediente no válido')
print('------------------------')
print(f'El precio de tu pizza es de {total} €')
