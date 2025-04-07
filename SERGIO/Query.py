from tabulate import tabulate
from TOTENA import Registers
 
def sales():
    print(tabulate(Registers.ventas, headers="keys",tablefmt="fancy_grid",colalign=("center","center","center","center","center","center","center","center")))

def ver_x_stock():
    stocks =[]
    stock = int(input("QUE STOCK DESEA BUSCAR: "))
    for i in Registers.ventas:
        if i["STOCK"] == stock:
            stocks.append(i)
    if stocks:
        print(tabulate(stocks, headers="keys",tablefmt="fancy_grid",colalign=("center","center","center","center","center","center","center","center")))
    else:
        print("NO SE ENCONTRO VENTAS CON ESTE STOCK")
print("")
