diccionario = {"Nombre":"Oliver","Edad":17,"Barrio":"Rio prado"}
print(diccionario)
print(type(diccionario))
#Buscar el valor de x llave del diccionario y 
#buscar el segundo dato que contiene la subDiccionario
print(diccionario["Nombre"][1])
diccionario["Nombre"]="Oli"
print(diccionario)
print(type(diccionario))
print(diccionario["Nombre"])

#recorrer un diccionario por llaves
for i in diccionario:
    print(i)

#Recorrer un diccionario por valor    
    for valor in diccionario:
        print(diccionario[valor])

#Imprimir las llaves y valores de un diccionario
for llave , valor in diccionario.items():
            print(llave,valor)

#Limpiar un diccionario
#diccionario.clear() #ESTO LIMPIA EL DICCIONARIOOOOOOO
print(diccionario)

#Guardar las llaves de un diccionario en una lista
listallaves=diccionario.keys()
print(listallaves)

#Guardar los valores de un diccionario en una lista
listavalores=diccionario.values()
print(listavalores)

#Eliminar una llave de un diccionario
#diccionario.pop("Nombre")
print(diccionario)

#Eliminar un elemento del diccionario de manera aleatoria}
#diccionario.popitem()
print(diccionario)

#Cruzar un diccionario a con uno b
diccionario2= {"Edad":23,"Barrio":"Ruitoque"}
diccionario.update(diccionario2)
print(diccionario)

