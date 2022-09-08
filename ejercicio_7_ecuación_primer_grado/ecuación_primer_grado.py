# Ejercicio No 7: Resolver una ecuación de primer grado.
print("-----------------------------")
print("----ECUACIÓN-PRIMER-GRADO----")
print("-----------------------------")
print("")

#input
a = int(input("Ingresa el valor de a"))
b = int(input("Ingresa el valor de b"))

#proceso y output
print("La ecuación es: {}x + {} = 0 ".format(a,b))


if a != 0:
    x = -b/a
    print("La respuesta es: x = {}".format(x))
else:
    if b == 0:
        print("La ecuación no tiene solución")
    else:
        print("La ecuación no tiene solución")