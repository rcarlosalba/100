dias = int(input("Ingresa la cantidad de dias: "))
horas = int(input("Ingresa la cantidad de horas: "))
minutos = int(input("Ingresa la cantidad de minutos: "))
segundos = int(input("Ingresa la cantidad de segundos: "))


def convertir_a_milisegundos(dias, horas, minutos, segundos):
    dias = dias * 86400000
    horas = horas * 3600000
    minutos = minutos * 60000
    segundos = segundos * 1000
    print(f'Eso da un total de: {
          dias + horas + minutos + segundos} milisegundos')


convertir_a_milisegundos(dias, horas, minutos, segundos)
