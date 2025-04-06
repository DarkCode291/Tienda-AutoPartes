import Query 
from tabulate import tabulate

def sales():
    print(tabulate(Query.ventas, headers="keys"))


def buscar_x_descripcion():
    decriptions = []
    desc = input("QUE PRODUCTO DESEA BUSCAR POR DESCRIPCION: ")
    for venta in Query.ventas:
        if venta["DESCRIPTION"].lower() == desc.lower():
            decriptions.append(venta)
        
    if decriptions:
        print(tabulate(decriptions, headers="keys"))
    else:
        print("NO SE ENCONTRO VENTAS CON ESTA DESCRIPCION")

def buscar_x_fecha():
     date = []
     busc = input("QUE PRODUCTO DESEA BUSCAR POR FECHA: ")
     for vusc in Query.ventas:
          if vusc["DATE"].lower() == busc.lower():
               date.append(vusc)
     if date:
        print(tabulate(date, headers="keys"))
     else:
        print("NO SE ENCONTRO VENTAS CON ESTA FECHA")

def buscar_x_comprador():
     name = []
     busc = input("QUE PRODUCTO DESEA BUSCAR POR NOMBRE(ESRIBIR NOMBRE CON APELLIDO): ")
     for vusc in Query.ventas:
          if vusc["BUYER NAME"].lower() == busc.lower():
               name.append(vusc)
     if name:
        print(tabulate(name, headers="keys"))
     else:
        print("NO SE ENCONTRO VENTAS CON ESTE NOMBRE")
