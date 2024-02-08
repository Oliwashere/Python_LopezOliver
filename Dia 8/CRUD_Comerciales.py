import json

def guardar_data(data):
    with open("data.json", "w") as file:
        json.dump(data, file, indent=2)

def crear_cliente(nuevo_cliente):

    clientes = data["ventas"]["clientes"]
    nuevo_cliente["id"] = max(cliente["id"] for cliente in clientes) + 1
    clientes.append(nuevo_cliente)
    guardar_data(data)

def read_comerciales(data):

    comerciales = data["ventas"]["comerciales"]

    print("")
    print("***************")
    print("* COMERCIALES * --------------")
    print("***************")
    print("")

    for comercial in comerciales:
        print(f"ID Comercial: {comercial['id']}")
        print(f"Nombre: {comercial['nombre']}")
        print(f"Primer apellido: {comercial['apellido1']}")
        print(f"Segundo apellido: {comercial['apellido2']}")
        print(f"Comisión: {comercial['comisión']:.2f}")
        print("------------------------------") 

    return comerciales

def actualizar_cliente(id_cliente, nuevos_datos):

    clientes = data["ventas"]["clientes"]
    
    for cliente in clientes:
        if cliente["id"] == id_cliente:
            cliente.update(nuevos_datos)
            break
    
    guardar_data(data)

def eliminar_cliente(id_cliente):

    clientes = data["ventas"]["clientes"]
    
    for cliente in clientes:
        if cliente["id"] == id_cliente:
            clientes.remove(cliente)
            break
    
    guardar_data(data)

nuevo_cliente = {"nombre": "Oli", "apellido1": "Lopez", "ciudad": "Giron", "categoría": 150}
crear_cliente(nuevo_cliente)

with open("data.json", "r") as file:
    data = json.load(file)

listado_comerciales = read_comerciales(data)