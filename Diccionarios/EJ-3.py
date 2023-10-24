diccionario={'Platano':1.35,'Manzana':0.8,'Pera':0.85,'Naranja':0.7}
fruta=input("Introduzca una fruta: ")
kg=int(input("Introduzca el numero de Kg que quiera comprar: "))
if fruta in diccionario:
    print("El precio es",kg*diccionario.get(fruta),"€")
else:
    print("La fruta no se comercializa en este establecimiento")

