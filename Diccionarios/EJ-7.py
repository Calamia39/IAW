cont=0
t=0
lista_compra={}
if cont == 0:
    while cont != 1:
        articulo = input("Escriba el articulo a añadir: ")
        valor = int(input("Escriba valor del articulo a añadir: "))
        lista_compra[articulo]=valor
        cont = input("Parar la lista introduce un 0, si no pon 1: ")
        if cont == "0":
            break
    for i in lista_compra:
        print("Articulo",i,"\n")
        t=lista_compra.get(i)+t
print("total",t)       
       