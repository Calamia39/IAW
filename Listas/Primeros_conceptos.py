#Tubla se crean con parentesis
Tupla1 = ("Casa","baño","salon")
#Lista con corchetes
Lista1 = ["Casa","baño","salon"]

#acceso a listas y tuplas
Objetos = ["casa","coche","puerta"]
Numeros = [111,222,333,444,555,666]
Cosas = ("reloj","coche","toalla","pc","PIPO")
Num = (1,2,3,4,55)

Objetos[1]

print(Objetos)


#Cortando listas y tuplas


Numeros[0:3]
#Selecciona parte de la lista pero no elimina 
#lo que no esta seleccionado
print(Numeros)

Numeros[:-2] #coge los valores sin incluir el -2
#el numero negativo, recorre la tabla al reves empezando por -1
Numeros[-2] #teda el 555


#Metodos de listas


#Append

Lista2 = ["Juan","Pedro","Alfonso","David","Yolanda"]
#vamos a añadir un nombre a la lista actual
Lista2.append("Alex")
print(Lista2)
    #inserta a Alex en la ultima posicion
  
    
#Extender una lista

Lista2.extend("JOSE")
print(Lista2)
#podemos extender una lista a otra
Lista2.extend(Lista1)
print(Lista2)

#insertar en una lista


Lista2.insert(1, "Alex") #Se cargo la primera Lista2
print(Lista2)
    #Insert te va a insertar en una posicion especifica
    

#metodos para eliminar elementos de una lista


#pop
Lista2.pop(1)#cojo la lista modificada anterior
print(Lista2) #elimina a Alex

#remuve
Lista2.remove("Juan")
#no vale poner una posicion de la lista
#es para eliminar una cosa concreta
print(Lista2)


#Funcion range
range(5)    #Da un rango del 0 al 5
x = list(range(5)) #metes el rango en una lista con la funcion list 
print(x)
x = list(range(8))
print(x)

#puedes poner un rango que empiece por un numero concreto llegue
#a otro. Tambien piedes hacer que salte los numeros que indiques
x = list(range(2,20,2))
print(x)









