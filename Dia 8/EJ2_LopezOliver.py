#2. Devuelve todos los datos de los dos pedidos de mayor valor.

import json

def obtener_dos_pedidos_mayor_valor(data):
 
    pedidos = data["ventas"]["pedidos"]

    pedidos_ordenados = sorted(pedidos, key=lambda x: x["total"], reverse=True)

    dos_pedidos_mayor_valor = pedidos_ordenados[:2]

    for pedido in dos_pedidos_mayor_valor:
        print(f"ID Pedido: {pedido['id']}")
        print(f"Total: ${pedido['total']:.2f}")
        print(f"Fecha de realización: {pedido['fecha']}")
        print(f"ID Cliente: {pedido['id_cliente']}")
        print(f"ID Comercial: {pedido['id_comercial']}")
        print("------------------------------")

    return dos_pedidos_mayor_valor

with open("data.json", "r") as file:
    data = json.load(file)

dos_pedidos_mayor_valor = obtener_dos_pedidos_mayor_valor(data)
