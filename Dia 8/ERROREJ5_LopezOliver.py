#5. Devuelve un listado con el nombre y los apellidos de los comerciales que tienen una 
#comisión entre 0.05 y 0.11.

import json

def obtener_comerciales_comision(data, comision_min, comision_max):
    # Obtener la lista de comerciales
    comerciales = data["ventas"]["comerciales"]

    # Filtrar los comerciales con comisión entre comision_min y comision_max
    comerciales_filtrados = [comercial for comercial in comerciales if comision_min <= comercial["comisión"] <= comision_max]

    # Mostrar el listado de comerciales
    for comercial in comerciales_filtrados:
        nombre_completo = f"{comercial['nombre']} {comercial['apellido1']} {comercial.get('apellido2', '')}"
        print(f"Nombre completo: {nombre_completo}")
        print(f"Comisión: {comercial['comisión']}")
        print("------------------------------")

    return comerciales_filtrados

# Cargar el archivo JSON desde un archivo externo
 # Reemplaza con la ruta correcta a tu archivo data.json
with open("data.json", "r") as file:
    data = json.load(file)

# Definir el rango de comisiones
comision_min = 0.05
comision_max = 0.11

# Obtener y mostrar el listado de comerciales con comisión entre 0.05 y 0.11
comerciales_filtrados = obtener_comerciales_comision(data, comision_min, comision_max)
