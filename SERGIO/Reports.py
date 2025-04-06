import Query 
from tabulate import tabulate

def sales():
    print(tabulate(Query.ventas, headers="keys",tablefmt="fancy_grid",colalign=("center","center","center","center","center","center","center","center")))


def buscar_x_descripcion():
    decriptions = []
    desc = input("QUE PRODUCTO DESEA BUSCAR POR DESCRIPCION: ")
    for venta in Query.ventas:
        if venta["DESCRIPTION"].lower() == desc.lower():
            decriptions.append(venta)
        
    if decriptions:
        print(tabulate(decriptions, headers="keys",tablefmt="fancy_grid",colalign=("center","center","center","center","center","center","center","center")))
    else:
        print("NO SE ENCONTRO VENTAS CON ESTA DESCRIPCION")

def buscar_x_fecha():
    date = []
    busc = input("QUE PRODUCTO DESEA BUSCAR POR FECHA: ")
    for i in Query.ventas:
        if i["DATE"].lower() == busc.lower():
            date.append(i)
    if date:
        print(tabulate(date, headers="keys"))
    else:
        print("NO SE ENCONTRO VENTAS CON ESTA FECHA")

def buscar_x_comprador():
    name = []
    busc = input("QUE PRODUCTO DESEA BUSCAR POR NOMBRE (ESRIBIR NOMBRE CON APELLIDO): ")
    for i in Query.ventas:
        if i["nComprador"].lower() == busc.lower():
            name.append(i)
    if name:
        print(tabulate(name, headers="keys"))
    else:
        print("NO SE ENCONTRO VENTAS CON ESTE NOMBRE")

sales()

