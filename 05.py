str1 = set(input('Ingresa un texto: '))
str2 = set(input('Ingresa otro texto: '))

one_but_not_two = (str1 - str2)
two_but_not_one = (str2 - str1)

print(f'Caracteres en el primer texto pero no en el segundo: {
      one_but_not_two}')
print(f'Caracteres en el segundo texto pero no en el primero: {
      two_but_not_one}')
