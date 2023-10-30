fecha=str(input("Dame una fecha DD/MM/YYYY : "))
dia=fecha[0:2]
mes=int(fecha[3:5])
ano=fecha[6:]
meses={1:'Enero',2:'Febrero',3:'Marzo',4:'Abril',5:'Mayo',6:'Junio',7:'Julio',8:'Agosto',9:'Septiembre',10:'Octubre',11:'Noviembre',12:'Diciembre'}
if mes in meses:
    print(dia,"de",meses.get(mes),"de", ano)