def area_figura():
    lados = float(input("¿Cuántos lados tiene la figura? "))
    longitud = float(
        input("¿Cuánto mide la medida uno de los lados de la figura? "))
    apotema = float(input("¿Cuánto mide la apotema de la figura? "))
    perimetro = lados * longitud
    area = (perimetro * apotema) / 2
    if lados == 3:
        print("El área del triángulo es: ", area)
    elif lados == 4:
        print("El área del cuadrado es: ", area)
    elif lados == 5:
        print("El área del pentágono es: ", area)
    else:
        print(f"Es un polígono con {lados} y un área de: {round(area)}.")


area_figura()
