diccionario = {}
palabras = input("Escriba las palabras en formato: - hola:hello,perro:dog,casa:house -: ")
for i in palabras.split(","):
    clave, valor = i.split(':')
    diccionario[clave] = valor

frase = input("Introduce una frase en español: ")

for j in frase.split(" "):
    if j in diccionario:
        print(diccionario[j],end=" ")
    else:
        print(j,end=" ")
