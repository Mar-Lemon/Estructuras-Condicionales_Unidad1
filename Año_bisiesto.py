# 2.Año bisiesto
# Solicita un año e indica si es bisiesto o no.
# (Un año es bisiesto si es divisible entre 4 pero no entre 100, o si es divisible entre 400).
print("--- Año bisiesto---")
bis_año = int(input("Ingresa un año: "))

# Verificación de las condiciones para ser año bisiesto
if (bis_año % 4 == 0 and bis_año % 100 != 0) or (bis_año % 400 == 0):
    print(f"El año {bis_año} es bisiesto.")
else:
    print(f"El año {bis_año} no es bisiesto.")
    