diccionario = {'EURO':'€','DOLLAR':'$','YEN':'Y'}
divisa = input("Escriba una divisa: ")
if divisa in diccionario:
    print(divisa,"Tiene el simbolo:",diccionario.get(divisa))
else:
    print("La divisa no esta en el diccionario")