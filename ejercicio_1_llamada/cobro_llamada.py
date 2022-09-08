# Taller  ejercicio No.1: cobro de llamada.

print("--------------------------")
print("-----COBRO-DE-LLAMADA-----")
print("--------------------------")

#input
m = int(input("Ingresa la cantidad en minutos que duro la llamada: "))

#proceso
if m <= 3:
    cos_t = 300
else:
    min_a = m -3
    cos_a = min_a * 50
    cos_t = cos_a + 300

#output

print("--------------------------")
print("--------RESULTADOS--------")
print("--------------------------")
print("")
print("La llamada duro ", m,"minutos y tienes un costo de $",cos_t)
