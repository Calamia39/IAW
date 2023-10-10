inversion = float (input("Ingrese la cantidad a invertir: "))
interes = float (input("Ingrese el interés anual: "))
anios = int (input("Ingrese el número de años: "))


for x in range(anios):
    inversion = inversion * (1 + interes/100)
    print("El capital obtenido será $" + str(round(inversion, 2)))