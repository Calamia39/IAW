# Crear una lista para almacenar las palabras
palabras = []

# Solicitar palabras al usuario hasta que ingrese "fin"
while True:
    palabra = input("Ingrese una palabra (o escriba 'fin' para detenerse):")
    
    if palabra == 'fin':
        break
    
    palabras.append(palabra)

# Solicitar un número entero
try:
    longitud_minima = int(input("Ingrese un número entero para la longitud mínima: "))
except ValueError:
    print("No ingresó un número entero válido.")
    exit()

# Filtrar y mostrar las palabras con longitud mayor a la longitud mínima
palabras_filtradas = [palabra for palabra in palabras if len(palabra) > longitud_minima]

if palabras_filtradas:
    print("Palabras con longitud mayor a", longitud_minima, ":", palabras_filtradas)
else:
    print("No hay palabras con longitud mayor a", longitud_minima)