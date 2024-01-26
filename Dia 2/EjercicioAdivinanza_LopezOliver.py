## -------------------------------
## ------- EJERCICIO 2 -----------
## -------------------------------

# ---- Juego de adivinanza ----

def juego_adivinanza():
    numero_secreto = random.randint(1, 100)
    intentos = 0

    print("Bienvenido al juego de adivinanza. Adivina el número secreto entre 1 y 100.")

    while True:
        try:
            suposicion = int(input("Introduce tu suposición: "))
        except ValueError:
            print("Por favor, introduce un número válido.")
            continue

        intentos += 1

        if suposicion == numero_secreto:
            print(f"¡Felicidades! Has adivinado el número secreto {numero_secreto} en {intentos} intentos.")
            break
        elif suposicion < numero_secreto:
            print("El número secreto es mayor. Intenta de nuevo.")
        else:
            print("El número secreto es menor. Intenta de nuevo.")