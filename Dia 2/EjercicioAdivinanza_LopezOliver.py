## -------------------------------
## ------- EJERCICIO 2 -----------
## -------------------------------

# ---- Juego de adivinanza ----

import random # Función del sistema para generar números aleatorios

def main(): # función main
    print("En este programa jugarás a adivinar un número que se encuentra entre 1 y 100 en tan solo 10 intentos")
    print()
    print("Cada que ingreses un número se indicará si es mayor o menor que el número aleatorio seleccionado")
    print()
    print("¡Buena suerte!")
    print()

    num = random.randint(1, 100) #  La función random.randint devuelve un número entero aleatorio en el intervalo cerrado
    intentos = 10 # a la variable "intentos" se le asigna 10

    while intentos > 0: # while variable "intentos" sea menor a cero entonces
        try: # hacer
            adivin = int(input("Ingresa el número que crees que se eligió (de 1 a 100): ")) # a la variable "adivin" se le asigna el número ingresado por el usuario
            if adivin < 1 or adivin > 100: # if variable "adivin" es menor a 1 o es mayor a 100 entonces
                print("Lo siento, debes ingresar un número entre 1 y 100.") # print("mensaje el cual sale si elegimos un número fuera del rango 1-100")
                continue # el comando "continue" pasa a la siguiente iteración saltando el código pendiente
        except ValueError: # el comando except se usa para repetir el código hasta que el número ingresado sea válido
            print("Lo siento, debes ingresar un número válido.")
            continue # el comando "continue" pasa a la siguiente iteración saltando el código pendiente

        intentos -= 1 # se le resta 1 a la variable intentos la cual pasó de 10 a 9

        if adivin < num: # if variable "adivin" es menor que la variable "num" entonces
            print(adivin,"Es menor que el número. Intenta de nuevo.") # print (variable adivin(número ingresado por el usuario)"mensaje indicando que es menor")
        elif adivin > num: # elif (usado para si no se cumple el if anterior usar este sin recurrir a else) variable "adivin" es mayor que la variable "num"
            print(adivin,"Es mayor que el número. Intenta de nuevo.") # print (variable adivin(número ingresado por el usuario)"mensaje indicando que es mayor")
        else: # else usado para dar una ultima condicion en caso de no cumplir las anteriores
            print(f"¡Felicidades! ¡Has adivinado el número en {11 - intentos} intentos.") # print (f-string inicio"Texto final{parámetros del f-string}texto restante")
            return # retorno

    print(f"Lo siento, has agotado tus intentos. El número era {num}.") # print (f-string inicio"texto final{parámetro}texto restante")

if __name__ == "__main__": #if usado para lanzar la función "main" completa anteriormente definida
    main()


if __name__ == "__main__": #if usado para lanzar la función "main" completa anteriormente definida
    main()

## Desarrollado por OLIVER EDUARDO LOPEZ PEREZ - 1097911715
