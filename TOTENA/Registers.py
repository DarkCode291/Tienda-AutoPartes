from tabulate import tabulate
import TOTENA.List_Sale as List_Sale
while True:
    print("-------------------------------------")
    print("|           AGREGAR VENTA           |")
    print("-------------------------------------")
    
    venta = {
        "ID": input("\nID del producto: "),
        "DES": input("Descripción del producto: "),
        "NUM PRODUCT": input("Número del producto: "),
        "AMOUNT": int(input("Cantidad: ")),
        "STOCK": int(input("Stock disponible: ")),
        "BUYER NAME": input("Nombre del comprador: "),
        "CC": int(input("Cédula del comprador: ")),
        "DATE": input("Fecha (dd/mm/aaaa): ")
    }

    List_Sale.ventas.append(venta)

    if input("QUIERES AGREGAR OTRA VENTA? (escriba 'fin' para salir): ").lower() == "fin":
        break

print(tabulate(List_Sale.ventas, headers="keys", tablefmt="fancy_grid"))
