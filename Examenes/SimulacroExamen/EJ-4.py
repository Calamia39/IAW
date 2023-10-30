diccionario={}
while True:
    InformacionE= input("Introduzca el elemento que se quiera introducir (escriba 'fin' para detenerse): ")
    if InformacionE  == 'fin':
        break
    valorE = input("\n Ingrese la informacion del elemento (escriba 'fin' para detenerse): ")
    if valorE  == 'fin':
        break
    diccionario[InformacionE]=valorE
    print(diccionario)
    
    