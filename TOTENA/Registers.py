ventas = [
    {
        "ID": 101,
        "DP": "Filtro de aceite",
        "C_VENDIDO": 2,
        "STOCK": 48,
        "COMPRADOR": "Carlos Perez",
        "CEDULA": 1002457890,
        "FECHA": "2025-04-01"
    }
]

compradores = [
    {
        "NOMBRE": "BRAYAN",
        "CEDULA": 1120865580
    }
]

from tabulate import tabulate
from colorama import Fore,init, Style; init(autoreset=True)
import datetime
import random

def register_sale():
    register = {}
    while(True):
        try:
            while(True):
                id_producto = generar_id()
                valor = validar_id(id_producto)
                if(valor):
                    descripcion = input("INGRESE LA DESCRIPCION DEL PRODUCTO: ")
                    while(True):
                        try:
                            cantidad_vendida = int(input("INGRESE LA CANTIDAD VENDIDA: "))
                            break
                        except ValueError:
                            print(f"{Fore.RED+Style.BRIGHT}ERROR INGRESE UN VALOR VALIDO")
                    stock = 50
                    stock -= cantidad_vendida
                    nombre = input("INGRESE EL NOMBRE DEL COMPRADOR: ").upper()
                    while True:
                        try:
                            cedula = int(input(f"INGRESE LA CEDULA DE {nombre}: "))
                            valor = validar_cedula(cedula)
                            if valor:
                                break
                            else:
                                print(f"{Fore.RED+Style.BRIGHT}ERROR LA CEDULA YA EXISTE")
                        except ValueError:
                            print(f"{Fore.RED+Style.BRIGHT}ERROR INGRESE UN VALOR VALIDO")
                    fecha = datetime.date.today()
                    register.setdefault("ID",id_producto)
                    register.setdefault("DP",descripcion)
                    register.setdefault("C_VENDIDO",cantidad_vendida)
                    register.setdefault("STOCK",stock)
                    register.setdefault("COMPRADOR",nombre)
                    register.setdefault("CEDULA",cedula)
                    register.setdefault("FECHA",fecha)
                    ventas.append(register)
                    volver()
                    break
                    
                        
        except ValueError:
            print("ERROR INGRESA VALORES VALIDOS ")



def generar_id():
    id_producto = random.randint(0000,9999)
    return id_producto

def validar_id(id):
    for i in ventas:
        if id in i.values():
            return False
    return True

def validar_cedula(cedula):
    for i in compradores:
        if cedula in i.values():
            return False
    return True

def volver():
    volver = input("DESEAS REGISTRAR OTRA VENTA [S] o [N]").upper()
    if volver == "S":
        register_sale()
    else:
        exit()
    
register_sale()