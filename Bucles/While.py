i = int(input("Introduce la contraseña: "))
count = 1
while count < 3:
    if i == 1234:
        print("Accediendo...")
        break
    else:
        i = int(input("Contraseña incorrecta introduzcala de nuevo: "))
        count = count+1
if count >= 3:
    print("Ha superado el numero maximo de intentos llamando a @Policia")
    print("Consejo del sistema: !CORRA¡")