## -----------------------------------
## ------- EJERCICIO BUGFIX -----------
## -----------------------------------

# ---- Bugfix ----

## Código a Bugfix:
# def negate(num):
#    return -num
#
# def large_num(num):
#    res = (num > 10000)

# negate(1)
# neg_b = num
# print "b is big:", big

## Bug 1:

# Se debe poner "print(función(parámetro))" en lugar de simplemente "función(parámetro)"
# En este caso:
#
# negate(num) //Mal
# print(negate(num)) //Bien

## Bug 2:

# No hay condicional para large_num, esto se puede solucionar ingresando el siguiente codigo dentro
# de la función "large_num":
#
# if num > 10000:
#    print("El número",num,"es mayor a 10000")
#    return True
#

## Bug 3:

# Quitamos la linea de código:
#
# print "b is big:", big
#
# La cual sobra y de todas maneras estaba mal, todo lo que va en un print debe estar en paréntesis:
# En este caso sería:
#
# print ("b is big:", big)

## Codigo Bugfixeado

def negate(num):
    return -num

def large_num(num):
    if num > 10000:
        print("El número",num,"es mayor a mil")
        return True
    else:
        return False
    

print(large_num(100))
print(negate(1000000))

## Desarrollado por OLIVER EDUARDO LOPEZ PEREZ - 1097911715