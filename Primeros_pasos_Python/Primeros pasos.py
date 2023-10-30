#priba del dia 1
a=14;
b=5;
print("la suma de a+b=",a+b);

#Ejemplo de IF

dinerotengo = int( input("¿cuanto dinero tengo?"))
precioprod = int( input("¿cuanto vale el producto?"))

if ((dinerotengo - precioprod) >= 0):
    print("Puedo comprar el producto")
    print("Saldo restante", dinerotengo - precioprod)
else:
    print("no se puede comprar el producto")

#Ejemple de una funcion

def puedocomprarprod (dinerotengo , precioprod):

    if ((dinerotengo - precioprod) >= 0):
        print("Puedo comprar el producto")
        print("Saldo restante", dinerotengo - precioprod)
    else:
        print("no se puede comprar el producto")
        
dinerotengo = int( input("¿cuanto dinero tengo?"))
precioprod = int( input("¿cuanto vale el producto?"))

puedocomprarprod (dinerotengo , precioprod)

#ejemplo 

Valor1 = int(input("Dame el primer valor :"))
Valor2 = int(input("Dame el segundo valor :"))
Valor3 = int(input("Dame el tercero valor :"))

if (Valor1>Valor2):
    if(Valor1>Valor3):
        print("El valor mayor es :",Valor1)
elif (Valor2>Valor3):
    print("El valor mayor es :",Valor2)
else:
    print("El valor mayor es",Valor3)

    
#implementar el ejemplo anterior en una funcion

def cualesmayor(Valor1,Valor2,Valor3):
    
    if (Valor1>Valor2):
        if(Valor1>Valor3):
            print("El valor mayor es :",Valor1)
    elif (Valor2>Valor3):
        print("El valor mayor es :",Valor2)
    else:
        print("El valor mayor es",Valor3)
        
Valor1 = int(input("Dame el primer valor :"))
Valor2 = int(input("Dame el segundo valor :"))
Valor3 = int(input("Dame el tercero valor :"))

cualesmayor(Valor1,Valor2,Valor3)


