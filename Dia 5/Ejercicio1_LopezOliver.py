## -------------------------------
## ------- EJERCICIO 1 -----------
## -------------------------------

# ---- Diccionario ----

dic={"Papas":3000,"Zanahorias":4000,"Tomates":2000,"Cebollas":1000}
print("ESTOS SON LOS PRODUCTOS DISPONIBLES CON SUS RESPECTIVOS PRECIOS")
print(dic)

print("INGRESE EL PRODUCTO ESCOGIDO")
prod = input()

if prod == "Papas":
    print("INGRESE LA CANTIDAD DE PAPAS QUE DESEA COMPRAR")
    cant = int(input())
    total = dic["Papas"] * cant
    print("EL PRECIO TOTAL DE TU COMPRA ES DE:")
    print(total)
elif prod == "Zanahorias":
    print("INGRESE LA CANTIDAD DE ZANAHORIAS QUE DESEA COMPRAR")
    cant = int(input())
    total = dic["Zanahorias"] * cant
    print("EL PRECIO TOTAL DE TU COMPRA ES DE:")
    print(total)   
elif prod == "Tomates":
    print("INGRESE LA CANTIDAD DE TOMATES QUE DESEA COMPRAR")
    cant = int(input())
    total = dic["Tomates"] * cant
    print("EL PRECIO TOTAL DE TU COMPRA ES DE:")
    print(total)
elif prod == "Cebollas":
    print("INGRESE LA CANTIDAD DE CEBOLLAS QUE DESEA COMPRAR")
    cant = int(input())
    total = dic["Cebollas"] * cant
    print("EL PRECIO TOTAL DE TU COMPRA ES DE:")
    print(total)
else:
    print("EL PRODUCTO:",prod,"NO SE ENCUENTRA EN LA LISTA")

## Desarrollado por OLIVER EDUARDO LOPEZ PEREZ - 1097911715