## -------------------------------
## ------- EJERCICIO 1 -----------
## -------------------------------

# ---- Serie de Fibonacci ----

print("Bienvenido a la serie de Fibonacci")
print()
print("¿Qué es la serie de Fibonacci?")
print()
print("Es una serie la cual empieza desde 0 y 1 y va de forma ascendente siendo el número siguiente la suma de si mismo con el número anterior")
print()
print("El programa va a repetirse hasta que el usuario ingrese 0 como valor")
print("En este programa podrás elegir hasta que término la secuencia va a continuar")
print()

def fibo(n): # def, nombre (parámetros)
    secuencia = [0, 1] # se crea la variable secuencia la cual cuenta con los valores iniciales (0, 1)
    while len(secuencia) < n: # while, lenght(variable "secuencia") sea menor a n
        secuencia.append(secuencia[-1] + secuencia[-2]) # variable "secuencia".adjuntar(variable secuencia[-1] + variable secuencia[-2]) (-1 y -2 para ubicar los valores correctamente)
    return secuencia # return variable "secuencia"

n = int(input("Ingrese el valor limitante: ")) # variable "n" se le es asignado un valor a ingresar por el usuario como entero
while n != 0: # while variable "n" no sea igual a cero
    secuencia = fibo(n) # variable "secuencia" ahora cambia sus variables de acuerdo a la función fibo
    print(secuencia) # mostrar en pantalla la secuencia resultante
    n = int(input("Ingrese un nuevo limitante para continuar o cero para terminar: ")) # variable "n" se le es asignado un nuevo valor a ingresar por el usuario como entero o se le da la opción de ingresar cero y terminar el programa

print("El programa ha terminado") # al ingresar cero soltará el anterior mensaje

## Desarrollado por OLIVER EDUARDO LOPEZ PEREZ - 1097911715