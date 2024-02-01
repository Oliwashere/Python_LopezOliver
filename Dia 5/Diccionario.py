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
for llavo , valor in Diccionario.items():
            