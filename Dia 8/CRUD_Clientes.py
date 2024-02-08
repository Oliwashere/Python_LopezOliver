import json

def read_clientes(data):

    clientes = data["ventas"]["clientes"]

    
    print("")
    print("************")
    print("* CLIENTES * ------------------")
    print("************")
    print("")


    for cliente in clientes:
        print(f"ID Cliente: {cliente['id']}")
        print(f"Nombre: {cliente['nombre']}")
        print(f"Primer apellido: {cliente['apellido1']}")
        print(f"Segundo apellido: {cliente['apellido2']}")
        print(f"Ciudad: {cliente['ciudad']}")
        print(f"Categoría: {cliente['categoría']}")
        print("------------------------------") 

    return clientes

with open("data.json", "r") as file:
    data = json.load(file)

listado_clientes = read_clientes(data)