#3. Devuelve un listado con los identificadores de los clientes que han realizado algún pedido.
# Tenga en cuenta que no debe mostrar identificadores que estén repetidos.

import json

def obtener_clientes_con_pedidos(data):

    pedidos = data["ventas"]["pedidos"]

    clientes_con_pedidos = set(pedido["id_cliente"] for pedido in pedidos)

    print("Identificadores de clientes con pedidos:")
    for cliente_id in clientes_con_pedidos:
        print(cliente_id)

    return clientes_con_pedidos

with open("data.json", "r") as file:
    data = json.load(file)

clientes_con_pedidos = obtener_clientes_con_pedidos(data)
