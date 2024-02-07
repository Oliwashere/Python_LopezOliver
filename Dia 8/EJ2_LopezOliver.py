#Devuelve todos los datos de los dos pedidos de mayor valor.

import json

def obtener_dos_pedidos_mayor_valor(data):
    # Obtener la lista de pedidos
    pedidos = data["ventas"]["pedidos"]

    # Ordenar la lista de pedidos por valor (de mayor a menor)
    pedidos_ordenados = sorted(pedidos, key=lambda x: x["total"], reverse=True)

    # Obtener los dos pedidos de mayor valor
    dos_pedidos_mayor_valor = pedidos_ordenados[:2]

    # Mostrar los datos de los dos pedidos de mayor valor
    for pedido in dos_pedidos_mayor_valor:
        print(f"ID Pedido: {pedido['id']}")
        print(f"Total: ${pedido['total']:.2f}")
        print(f"Fecha de realización: {pedido['fecha']}")
        print(f"ID Cliente: {pedido['id_cliente']}")
        print(f"ID Comercial: {pedido['id_comercial']}")
        print("------------------------------")

    return dos_pedidos_mayor_valor

# Cargar el archivo JSON
with open("data.json", "r") as file:
    data = json.load(file)

# Obtener y mostrar los datos de los dos pedidos de mayor valor
dos_pedidos_mayor_valor = obtener_dos_pedidos_mayor_valor(data)
