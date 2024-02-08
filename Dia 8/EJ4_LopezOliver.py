#4. Devuelve un listado de todos los pedidos que se realizaron durante el año 2017, 
#cuya cantidad total sea superior a 500€.

import json

def obtener_pedidos_2017_mayor_500(data):
    
    pedidos = data["ventas"]["pedidos"]

    pedidos_filtrados = [pedido for pedido in pedidos if pedido["fecha"].startswith("2017") and pedido["total"] > 500]

    for pedido in pedidos_filtrados:
        print(f"ID Pedido: {pedido['id']}")
        print(f"Total: ${pedido['total']:.2f}")
        print(f"Fecha de realización: {pedido['fecha']}")
        print(f"ID Cliente: {pedido['id_cliente']}")
        print(f"ID Comercial: {pedido['id_comercial']}")
        print("------------------------------")

    return pedidos_filtrados

with open("data.json", "r") as file:
    data = json.load(file)

pedidos_filtrados = obtener_pedidos_2017_mayor_500(data)
