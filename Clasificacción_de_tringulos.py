# Clasificación de triángulos
# Solicita al usuario las 3 longitudes de los lados de un triángulo.
# Indica si es equilátero, isósceles o escaleno.
print("---Clasificación de triángulos---")
# Solicitud de las longitudes de los tres lados
lado1 = float(input("Ingresa la longitud del primer lado: "))
lado2 = float(input("Ingresa la longitud del segundo lado: "))
lado3 = float(input("Ingresa la longitud del tercer lado: "))

# Verificación de que los lados formen un triángulo válido
if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    if lado1 == lado2 == lado3:
        print("El triángulo es Equilátero.")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("El triángulo es Isósceles.")
    else:
        print("El triángulo es Escaleno.")
else:
    print("Las medidas ingresadas no forman un triángulo válido.")
