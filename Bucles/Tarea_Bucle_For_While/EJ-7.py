key = "contraseña"
contrasena = input("Introduce la contraseña: ")
if key != contrasena:
    while key != contrasena:
        print("La contraseña no coincide")
        contrasena = input("Introduce la contraseña nuevamente: ")
    print("La contraseña coincide")
else:
    print("La contraseña coincide")

