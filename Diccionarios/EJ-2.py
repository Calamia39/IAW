diccionario = {}
nombre = input("Escriba su nombre: ")
edad =int( input("Escriba su edad: "))
direccion = input("Escriba su direccion: ")
tel =int( input("Escriba su telefono: "))
diccionario["Nombre"]=nombre
diccionario["Edad"]=edad
diccionario["Direccion"]=direccion
diccionario["Telefono"]=tel
print(diccionario.get("Nombre"),"tiene", diccionario.get("Edad"),"años, vive en", diccionario.get("Direccion"),"y su número de teléfono es", diccionario.get("Telefono")," .")
