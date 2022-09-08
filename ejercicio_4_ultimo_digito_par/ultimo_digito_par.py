# Taller  ejercicio No.4: Detector del ultimo dígito si es par o no lo es.

print("----------------------------------")
print("--------DETECTOR-PAR-O-IMPAR------")
print("----------------------------------")

#input
n = int(input("Ingresa un número de varios dígitos:"))


#process
p = n % 2
u = n % 10

if p == 0:
    r = "es par"
else:
    r = "no es par"

#output
print("------------------------------------")
print("-------------RESULTADOS-------------")
print("El ultimo numero es",u," y este",r)

