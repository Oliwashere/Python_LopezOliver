import json

def read_pedidos(data):

    pedidos = data["ventas"]["pedidos"]

    print("")
    print("***********")
    print("* PEDIDOS * ------------------")
    print("***********")
    print("")

    for pedido in pedidos:
        print(f"ID Pedido: {pedido['id']}")
        print(f"Total: ${pedido['total']:.2f}")
        print(f"Fecha de realización: {pedido['fecha']}")
        print(f"ID Cliente: {pedido['id_cliente']}")
        print(f"ID Comercial: {pedido['id_comercial']}")
        print("------------------------------") 

    return pedidos

with open("data.json", "r") as file:
    data = json.load(file)

listado_pedidos = read_pedidos(data)

#######################################

