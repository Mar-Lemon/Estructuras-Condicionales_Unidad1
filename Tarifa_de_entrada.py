# Tarifa de entrada
# Solicita la edad de una persona y muestra el costo de entrada a un parque:
# Menores de 12 años: $50
# De 12 a 17 años: $80
# Adultos (18 en adelante): $120

print("---Tarifa_de_entrega---")

# Solicitud de la edad
edad = int(input("Ingresa tu edad: "))

# Determinación de la tarifa según el rango de edad
if edad < 0:
    print("Error: Ingresa una edad válida.")
elif edad < 12:
    print("Costo de entrada: $50")
elif 12 <= edad <= 17:
    print("Costo de entrada: $80")
else:
    print("Costo de entrada: $120")