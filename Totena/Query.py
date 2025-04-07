from tabulate import tabulate


def sales(ventas):
    print(tabulate(ventas, headers="keys",tablefmt="fancy_grid",colalign=("center","center","center","center","center","center","center")))

def ver_x_stock(ventas):
    stocks =[]
    stock = int(input("QUE STOCK DESEA BUSCAR: "))
    for i in ventas:
        if i["STOCK"] == stock:
            stocks.append(i)
    if stocks:
        print(tabulate(stocks, headers="keys",tablefmt="fancy_grid",colalign=("center","center","center","center","center","center","center")))
    else:
        print("NO SE ENCONTRO VENTAS CON ESTE STOCK")


