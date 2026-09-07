# Conversor de calificaciones
# Pide una calificación numérica (0–100) y muestra la equivalencia en letra:
# 90–100: A
# 80–89: B
# 70–79: C
# 60–69: D
# Menor a 60: F
 
print("---Conversor de calificaciones---")

# Solicitud de la calificación
calificacion = float(input("Ingresa la calificación numérica (0-100): "))

# Validación y conversión a letra
if 90 <= calificacion <= 100:
    print("Calificación: A")
elif 80 <= calificacion < 90:
    print("Calificación: B")
elif 70 <= calificacion < 80:
    print("Calificación: C")
elif 60 <= calificacion < 70:
    print("Calificación: D")
elif 0 <= calificacion < 60:
    print("Calificación: F")
else:
    print("Error: La calificación debe estar entre 0 y 100.")
    