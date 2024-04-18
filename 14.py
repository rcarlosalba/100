es_primo = int(input("Introduce un número para saber si es primo: "))
if es_primo < 2:
    print("El número no es primo.")
else:
    for i in range(2, es_primo):
        if es_primo % i == 0:
            print("El número no es primo.")
            break
    else:
        print("El número es primo.")
