# Bucles [Python]
# Ejemplos de clase

# Autor: Inove Coding School
# Version: 3.0

# Ejemplos con bucle While infinito + break

# Hasta que el usuario no ingrese una
# operación válida, el sistema
# continuará solicitando que ingrese
# una opción de operación
while True:
    print("Ingrese operación a realizar:")
    print("1- Suma")
    print("2- Resta")
    operacion = str(input())

    if operacion == "1" or operacion == "2":
        print("¡Se termina el bucle!")
        break

print(operacion)
print("FIN")




