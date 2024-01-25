## ---------------------------------
## ---- Ejercicio 1 ----
## ---------------------------------

# Impresión en consola
print("Hola MundOwO")

# ---- Datos primitivos ----

# 1. String
texto = "Campus"
print(texto)
print(type(texto))
# 2. Int
numeroEntero = 1
print(numeroEntero)
# 3. Float
numeroDecimal = 3.1
print(numeroDecimal)
# 4. Double
numeroDecimalLargo = 3.14167582737283
print(numeroDecimalLargo)
# 5. Boolean
booleano = True
print(booleano)

# ---- Entradas parte del usuario ----

entradaUsuario = input("Ingresa tu nombre: ")
print("Tu nombre es:",entradaUsuario)

# ---- Entradas parte del usuario con definición de tipo de dato primitivo ----

entradaUsuarioNumero = int(input("Ingresa tu edad: "))
print("Tu edad es:",entradaUsuarioNumero)

# ---- Ciclos ----

# Ciclo "for"
for i in range(5,10,2): # For contador in range (Desde,hasta,pasos):
    print(i)

# Ciclo "while"
booleanito = True
while booleanito == True: # While condición a_cumplir :
    print("Sigo vivo")
    booleanito = False

# ---- Condicionales ---- 
texto1 = "Campus"
if texto1 == "Campus":
    print("Soy Campus")
else:
    print("No soy Campus")

## ---- Funciones ----
    
# Con parámetros y con retorno
def suma(a, b):  # def, nombre de la función, (parámetros)
    resultado = a + b # Variable a retornar
    return resultado  # return, nombre de la anterior variable

print(suma(2, 2)) # print, (nombre de la función(parámetros))

# Sin parámetros y sin retorno
def mensaje(): # def, nombre de la función
    print("Hola marcianos") # print, mensaje



## ---- Arreglos ----    

## Desarrollado por OLIVER EDUARDO LOPEZ PEREZ - 1097911715