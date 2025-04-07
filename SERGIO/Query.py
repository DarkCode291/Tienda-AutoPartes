from tabulate import tabulate


ventas = [
    {
        "ID": 101,
        "DES": "Filtro de aceite",
        "NUM PRODUCT": "FO-123",
        "AMOUNT": 2,
        "STOCK": 48,
        "BUYER NAME": "Carlos Perez",
        "CC": 1002457890,
        "DATE": "2025-04-01"
    },
    {
        "ID": 102,
        "DES": "Pastillas de freno",
        "NUM PRODUCT": "PF-456",
        "AMOUNT": 1,
        "STOCK": 99,
        "BUYER NAME": "Laura Gomez",
        "CC": 1003987654,
        "DATE": "2025-04-02"
    },
    {
        "ID": 101,
        "DES": "Filtro de aceite",
        "NUM PRODUCT": "FO-123",
        "AMOUNT": 3,
        "STOCK": 45,
        "BUYER NAME": "Andres Torres",
        "CC": 1005123789,
        "DATE": "2025-04-03"
    },
    {
        "ID": 103,
        "DES": "Aceite sintetico",
        "NUM PRODUCT": "AS-789",
        "AMOUNT": 5,
        "STOCK": 20,
        "BUYER NAME": "Sofia Martinez",
        "CC": 1009876543,
        "DATE": "2025-04-04"
    }
]


def sales():
    print(tabulate(ventas, headers="keys",tablefmt="fancy_grid",colalign=("center","center","center","center","center","center","center","center")))

def ver_x_stock():
    stocks =[]
    stock = int(input("QUE STOCK DESEA BUSCAR: "))
    for i in ventas:
        if i["STOCK"] == stock:
            stocks.append(i)
    if stocks:
        print(tabulate(stocks, headers="keys",tablefmt="fancy_grid",colalign=("center","center","center","center","center","center","center","center")))
    else:
        print("NO SE ENCONTRO VENTAS CON ESTE STOCK")

