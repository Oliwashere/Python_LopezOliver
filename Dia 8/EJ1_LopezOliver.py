#1. Devuelve un listado con todos los pedidos que se han realizado.
# Los pedidos deben estar ordenados por la fecha de realización,
# mostrando en primer lugar los pedidos más recientes.

import json

def obtener_listado_pedidos(data):
    # Obtener la lista de pedidos
    pedidos = data["ventas"]["pedidos"]

    # Ordenar la lista de pedidos por fecha de realización (de más reciente a más antiguo)
    pedidos_ordenados = sorted(pedidos, key=lambda x: x["fecha"], reverse=True)

    # Mostrar el listado de pedidos
    for pedido in pedidos_ordenados:
        print(f"ID Pedido: {pedido['id']}")
        print(f"Total: ${pedido['total']:.2f}")
        print(f"Fecha de realización: {pedido['fecha']}")
        print(f"ID Cliente: {pedido['id_cliente']}")
        print(f"ID Comercial: {pedido['id_comercial']}")
        print("------------------------------") 

    return pedidos_ordenados

# Cargar el archivo JSON
with open("data.json", "r") as file:
    data = json.load(file)

# Obtener y mostrar el listado de pedidos ordenados
listado_pedidos = obtener_listado_pedidos(data)












