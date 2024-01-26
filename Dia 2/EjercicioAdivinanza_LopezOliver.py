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
            adivin = int(input("Ingresa el número que crees que se eligió (de 1 a 100): ")) # 
            if adivin < 1 or adivin > 100:
                print("Lo siento, debes ingresar un número entre 1 y 100.")
                continue
        except ValueError:
            print("Lo siento, debes ingresar un número válido.")
            continue

        intentos -= 1

        if adivin < num:
            print(adivin,"Es menor que el número. Intenta de nuevo.")
        elif adivin > num:
            print(adivin,"Es mayor que el número. Intenta de nuevo.")
        else:
            print(f"¡Felicidades! ¡Has adivinado el número en {11 - intentos} intentos.")
            return

    print(f"Lo siento, has agotado tus intentos. El número era {num}.")

if __name__ == "__main__":
    main()