from tabulate import tabulate
import TOTENA.List_Sale as List_Sale
def sales():
    print(tabulate(List_Sale.ventas, headers="keys",tablefmt="fancy_grid",colalign=("center","center","center","center","center","center","center","center")))

def ver_x_stock():
    stocks =[]
    stock = int(input("QUE STOCK DESEA BUSCAR: "))
    for i in List_Sale.ventas:
        if i["STOCK"] == stock:
            stocks.append(i)
    if stocks:
        print(tabulate(stocks, headers="keys",tablefmt="fancy_grid",colalign=("center","center","center","center","center","center","center","center")))
    else:
        print("NO SE ENCONTRO VENTAS CON ESTE STOCK")

