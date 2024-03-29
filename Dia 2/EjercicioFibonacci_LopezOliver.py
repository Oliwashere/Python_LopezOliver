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

def fibo(n): # def, nombre (variable n (parámetro))
    secuencia = [0, 1] # se crea la variable secuencia la cual cuenta con los valores iniciales (0, 1)
    while len(secuencia) < n: # while, (variable "secuencia") sea menor a n
        secuencia.append(secuencia[-1] + secuencia[-2]) # variable "secuencia".adjuntar(variable secuencia[-1] + variable secuencia[-2]) (-1 y -2 para ubicar los valores correctamente)
    return secuencia # return variable "secuencia"

while True: # while, variable "True"
    try: # hacer
        n = int(input("Ingrese el valor limitante: ")) # variable "n" se le es asignado el valor ingresado por el usuario
        print()
        if n < 0: # if variable "n" es menor a cero entonces
            print("Error: El valor limitante debe ser positivo, por favor procura ingresar un número positivo entero") # mostrar mensaje de error
            print()
        else:
            break # break para parar el bucle
    except ValueError: # excepción de break si la variable "n" ingresada no es un número entero
        print("Error: El valor limitante debe ser un número entero, por favor procura ingresar un número positivo entero") # mostrar mensaje de error
        print()

while n != 0: # while variable "n" no sea igual a 0
    secuencia = fibo(n) # A la secuencia se le asigna la función fibo junto con el valor ingreso
    print(secuencia) # Mostrar la secuencia generada con base al valor limitante ingresado
    print()
    while True: # while, variable "True"
        try:
            n = int(input("Ingrese un nuevo valor limitante o ingrese 0 para finalizar el programa: ")) # a la variable "n" se le es asignado el valor ingresado por el usuario (si es cero terminará el programa)
            print()
            if n < 0: # if variable "n" es menor que cero entonces
                print("Error: El valor limitante debe ser positivo, por favor procura ingresar un número positivo entero") # mostrar mensaje de error
                print()
            else:
                break # break para parar el bucle
        except ValueError: # excepción de break si la variable "n" ingresada es un caracter y no es un número entero
            print("Error: El valor limitante debe ser un número entero, por favor procura ingresar un número positivo entero")
            print()

print("El programa ha terminado") # al ingresar cero soltará el anterior mensaje

## Desarrollado por OLIVER EDUARDO LOPEZ PEREZ - 1097911715