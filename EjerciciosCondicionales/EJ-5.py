diasem = input("Dame un dia de la semana (minusculas) :")

if (diasem == "lunes"):
    print("El dia de la semana es Lunes")
elif (diasem == "viernes"):
    print("El dia de la semana es Viernes")
elif (diasem == "sabado" or diasem == "domingo"):
    print("El dia de la semana es Sabado o Domingo")
else:
    print("El dia de la semana no esta dentro de nuestro horario de apertura")