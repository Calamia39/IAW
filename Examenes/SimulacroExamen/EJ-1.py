seguir=True
num=[]
suma=0
mult=1

while seguir: 
        num.append(int(input("Dame numeros enteros: ")))
        seguir=input("Seguir escribe SI, si no escribe NO: ")
        if seguir=="no":
            break
for i in num :
    suma=suma+i
    mult=mult*i
print("La suma de los numeros es: ",suma)
print("Su multiplicacion es: ", mult)
