# Bucles [Python]
# Ejemplos de clase

# Autor: Inove Coding School
# Version: 3.0

# Ejemplos con bucle While infinito + break

while True:
    print("Ingrese SALIR para terminar el bucle")
    entrada = str(input())
    # Pasar a minúsculas
    entrada = entrada.lower()
    if entrada == "salir":
        print("¡Se termina el bucle!")
        break

print("FIN")




