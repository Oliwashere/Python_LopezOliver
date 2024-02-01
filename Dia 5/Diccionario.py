Diccionario = {"Nombre":"Oliver","Edad":17,"Barrio":"Rio prado"}
print(Diccionario)
print(type(Diccionario))
#Buscar el valor de x llave del diccionario y 
#buscar el segundo dato que contiene la subDiccionario
print(Diccionario["Nombre"][1])
Diccionario["Nombre"]="Oli"
print(Diccionario)
print(type(Diccionario))
print(Diccionario["Nombre"])

#recorrer un Diccionario por llaves
for i in Diccionario:
    print(i)

#Recorrer un Diccionario por valor    
    for valor in Diccionario:
        print(Diccionario[valor])

#Imprimir las llaves y valores de un diccionario
for llave , valor in Diccionario.items():
            print(llave,valor)

#Limpiar un diccionario
#Diccionario.clear() #ESTO LIMPIA EL DICCIONARIOOOOOOO
print(Diccionario)

#Guardar las llaves de un diccionario en una lista
listallaves=Diccionario.keys()
print(listallaves)

#Guardar los valores de un diccionario en una lista
listavalores=Diccionario.values()
print(listavalores)

#Eliminar una llave de un diccionario
Diccionario.pop("Nombre")
print(Diccionario)