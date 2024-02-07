# Devuelve un listado con los identificadores de los clientes que han realizado algún pedido.
# Tenga en cuenta que no debe mostrar identificadores que estén repetidos.

import json

def obtener_clientes_con_pedidos(data):
    # Obtener la lista de pedidos
    pedidos = data["ventas"]["pedidos"]

    # Obtener identificadores únicos de clientes que han realizado algún pedido
    clientes_con_pedidos = set(pedido["id_cliente"] for pedido in pedidos)

    # Mostrar el listado de identificadores de clientes con pedidos
    print("Identificadores de clientes con pedidos:")
    for cliente_id in clientes_con_pedidos:
        print(cliente_id)

    return clientes_con_pedidos

# Cargar el archivo JSON
with open("data.json", "r") as file:
    data = json.load(file)

# Obtener y mostrar el listado de identificadores de clientes con pedidos
clientes_con_pedidos = obtener_clientes_con_pedidos(data)
