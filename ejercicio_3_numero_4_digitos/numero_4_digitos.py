# Taller  ejercicio No.3: número 4 digitos.

print("------------------------")
print("----NUMERO-4-DIGITOS----")
print("------------------------")
print("")

#input
n = int(input("Ingresa un número de varios dígitos: "))

#process

if n >= 1000:
    if n >= 10000:
        r = "es un número mayor a cuatro dígitos"
    else:
        r = "es un número de cuatro dígitos positivo"
else:
    r = "es un número menor de cuatro dígitos positivo"

#output
print("--------------------------")
print("---------RESULTADO--------")
print("El número", n,r)