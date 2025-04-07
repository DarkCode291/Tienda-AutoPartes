import Query 
from tabulate import tabulate


def buscar_x_descripcion():
    decriptions = []
    desc = input("QUE PRODUCTO DESEA BUSCAR POR DESCRIPCION: ").lower()
    for i in Query.ventas:
        if i["DES"].lower() == desc:
            decriptions.append(i)
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
        print(tabulate(date, headers="keys",tablefmt="fancy_grid",colalign=("center","center","center","center","center","center","center","center")))
    else:
        print("NO SE ENCONTRO VENTAS CON ESTA FECHA")

def buscar_x_comprador():
    name = []
    busc = int(input("INGRESE LA CEDULA DEL COMPRADOR: "))
    for i in Query.ventas:
        if i["CC"] == busc:
            name.append(i)
    if name:
        print(tabulate(name, headers="keys",tablefmt="fancy_grid",colalign=("center","center","center","center","center","center","center","center")))
    else:
        print("NO SE ENCONTRO VENTAS CON ESTE NOMBRE")

buscar_x_descripcion()