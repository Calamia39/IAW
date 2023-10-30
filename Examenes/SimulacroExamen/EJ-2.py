Lista=[]
seguir=True
m=0
M=0
j=""
while seguir: 
        Lista.append(input("Introduzca palabras: "))
        seguir=input("Seguir escribe SI, si no escribe NO: ")
        if seguir=="no":
            break 
for i in Lista:
    m=len(i)
    if m>M: 
        M=m
        j=i

print("La palabra mas larga es:",M," La palabra mas grande es: ",j)