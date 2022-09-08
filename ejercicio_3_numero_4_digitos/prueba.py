# Ejercicio 3 : Numero de 4 dijitos

print("------------------------------")
print("----NUMERO DE 4 DIJITOS-------")
print("------------------------------")

#input
n =  int(input("Dijite el numero de 4 dijitos : "))

#process
if n >= 1000:
    if n <= 10000:
        r = "es mayor de 4 dijitos"
    else:
        r = "es de 4 dijitos positvo"
else:
    r = "No es de 4 dijitos"

#output
print("---------------------")
print("----RESULTADOS-------")
print("---------------------")

print( "El numero",n ,r, )