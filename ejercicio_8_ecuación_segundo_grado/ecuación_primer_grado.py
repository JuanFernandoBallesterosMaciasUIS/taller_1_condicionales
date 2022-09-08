# Ejercicio No 8: Resolver una ecuación de segundo grado.
import math
print("-----------------------------")
print("---ECUACIÓN-SEGUNDO-GRADO----")
print("-----------------------------")
print("")

#input
a = float(input("Ingresa el valor de a: "))
b = float(input("Ingresa el valor de b: "))
c = float(input("Ingresa el valor de c: "))

#proceso
discri = (b*b) - (4*a*c)
if discri < 0:
    print("No tiene raíces reales")
else:
    if discri == 0:
        x = -b / (2 * a)
        print("La solución es {}".format(x))
    else:
        x1 = (-b + math.sqrt(discri)) / (2 * a)
        x2 = (-b - math.sqrt(discri)) / (2 * a)
        print("x1 = {} y x2 = {}".format(x1,x2))