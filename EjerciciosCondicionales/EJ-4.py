Valor1 = int(input("Dame el primer valor :"))
Valor2 = int(input("Dame el segundo valor :"))
Valor3 = int(input("Dame el tercero valor :"))

if (Valor1>Valor2):
    if(Valor1>Valor3):
        print("El valor mayor es :",Valor1)
    elif(Valor1==Valor3):
        print("El valor1 es igual a valor3")
elif (Valor2>Valor3):
    if (Valor2==Valor1):
        print("El valor1 es igual al valor 2")
    print("El valor mayor es :",Valor2)
elif (Valor2==Valor3):
    print("El valor2 es igual al valor 3")
else:
    print("El valor mayor es",Valor3)
