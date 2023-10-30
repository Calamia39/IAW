edad = int(input("¿Que edad tienes? : "))
salar = float(input("¿Cuanto ganas al mes?"))

if (edad > 16 and salar > 1000):
    print("Usted tiene que tributar a Hacienda. Muchas gracias.")
else:
    print("Usted no cumple con los requisitos necesarios para tributar. Sentimos no contar con su contribucion, Gracias.")