import List_Sale
from tabulate import tabulate

def agregar_ventas():
    while True:
        print("-------------------------------------")
        print("|           AGREGAR VENTA           |")
        print("-------------------------------------")
    
        venta = {
            "ID": int(input("ID DEL PRODUCTO: ")),
            "DES": input("DESCRIPCION DEL PRODUCTO: "),
            "NUM PRODUCT": input("NUMERO DEL PRODUCTO: "),
            "AMOUNT": int(input("CANTIDAD: ")),
            "STOCK": int(input("STOCK DISPONIBLE: ")),
            "BUYER NAME": input("NOMBRE DEL COMPRADOR: "),
            "CC": int(input("CEDULA DEL COMPRADOR: ")),
            "DATE": input("FECHA: (AAA/MM/DD): ")
        }

        List_Sale.ventas.append(venta)

        if input("QUIERES AGREGAR OTRA VENTA? (escriba 'fin' para salir): ").lower() == "fin":
            break
    print(tabulate(List_Sale.ventas, headers="keys", tablefmt="fancy_grid"))


def cambiar_info():
    cc_buscado = int(input("INGRESE CC DEL COMPRADOR PARA CAMBIAR INFO"))
    for i, venta in enumerate(List_Sale.ventas):
        if venta["CC"] == cc_buscado:
            print(tabulate([venta], headers="keys", tablefmt="fancy_grid",colalign=("center","center","center","center","center","center","center","center")))
            confirmar = input("ES ESTA LA VENTA QUE DESEA MODIFICAR? (S/N): ").lower()
            if confirmar == "s":
                print("\nINGRESE LA INFO DE LA VENTA ACTUALIZADA:")
                nueva_venta = {
                    "ID": int(input("ID DEL PRODUCTO: ")),
                    "DES": input("DESCRIPCION DEL PRODUCTO: "),
                    "NUM PRODUCT": input("NUMERO DEL PRODUCTO: "),
                    "AMOUNT": int(input("CANTIDAD: ")),
                    "STOCK": int(input("STOCK DISPONIBLE: ")),
                    "BUYER NAME": input("NOMBRE DEL COMPRADOR: "),
                    "CC": int(input("CEDULA DEL COMPRADOR: ")),
                    "DATE": input("FECHA: (AAA/MM/DD): ")
                }
                List_Sale.ventas[i] = nueva_venta
                print("\n VENTA ACTUALIZADA")
                break
    else:
        print("NO SE ENCONTRO LA VENTA.")

    print("\n VENTA ACTUALIZADA:")
    print(tabulate(List_Sale.ventas, headers="keys", tablefmt="fancy_grid",colalign=("center","center","center","center","center","center","center","center")))

cambiar_info()