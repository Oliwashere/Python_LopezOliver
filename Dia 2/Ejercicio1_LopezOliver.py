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

def fibo(n):
    secuencia = [0, 1]
    while len(secuencia) < n:
        secuencia.append(secuencia[-1] + secuencia[-2])
    return secuencia

n = int(input("Ingrese el valor limitante: "))
while n != 0:
    secuencia = fibo(n)
    print(secuencia)
    n = int(input("Ingrese un nuevo limitante para continuar o cero para terminar: "))

print("El programa ha terminado")    

## Desarrollado por OLIVER EDUARDO LOPEZ PEREZ - 1097911715