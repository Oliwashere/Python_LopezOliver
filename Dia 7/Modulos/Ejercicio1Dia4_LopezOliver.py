## -------------------------------
## ------- EJERCICIO 1 -----------
## -------------------------------

# ---- Cantidad de pares ----

import itertools

def encontrar_pares(n, k, A):
    pares = []  # Lista para almacenar los pares encontrados
    for i, j in itertools.combinations(range(n), 2): #Lo que dijo Helen
        if (A[i] + A[j]) % k == 0: 
            par = tuple(sorted((A[i], A[j])))
            if par not in pares:
                pares.append(par)
    return pares
Casos = []
lista_separada = []
lista_separada_numeros = []
T = int(input("T: "))
for t in range(T):
    nk = str(input(" "))
    lista_separada = nk.split(" ")
    caracteres_lista = len(lista_separada)
    lista_separada[-1] = int(lista_separada[-1])
    n = lista_separada[0]
    n = int(n)
    k = lista_separada[1]
    k = int(k)

    A = list(map(int, input(" ").split()))


    pares = encontrar_pares(n, k, A)

    Casos.append(len(pares))
for z in range(0,T,1):
    print(f"Caso #{z+1}: ",Casos[z])

    ## Desarrollado por OLIVER EDUARDO LOPEZ PEREZ - 1097911715