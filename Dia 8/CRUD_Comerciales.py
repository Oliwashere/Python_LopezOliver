import json

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

with open("data.json", "r") as file:
    data = json.load(file)

listado_comerciales = read_comerciales(data)