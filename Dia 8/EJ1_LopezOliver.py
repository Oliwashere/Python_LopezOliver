#1. Devuelve un listado con todos los pedidos que se han realizado.
#Los pedidos deben estar ordenados por la fecha de realización,
#mostrando en primer lugar los pedidos más recientes.

import json

def obtener_listado_pedidos(data):

    pedidos = data["ventas"]["pedidos"]

    pedidos_ordenados = sorted(pedidos, key=lambda x: x["fecha"], reverse=True)

    for pedido in pedidos_ordenados:
        print(f"ID Pedido: {pedido['id']}")
        print(f"Total: ${pedido['total']:.2f}")
        print(f"Fecha de realización: {pedido['fecha']}")
        print(f"ID Cliente: {pedido['id_cliente']}")
        print(f"ID Comercial: {pedido['id_comercial']}")
        print("------------------------------") 

    return pedidos_ordenados

with open("data.json", "r") as file:
    data = json.load(file)

listado_pedidos = obtener_listado_pedidos(data)












