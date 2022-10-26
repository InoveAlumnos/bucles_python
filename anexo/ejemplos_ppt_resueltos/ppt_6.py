# Bucles [Python]
# Ejemplos de clase

# Autor: Inove Coding School
# Version: 2.0

# Ejemplos con bucle While infinito + break

while True:
    entrada = str(input("Ingrese SALIR para terminar el bucle:\n"))
    # Pasar a minúsculas
    entrada = entrada.lower()
    if entrada == "salir":
        print("¡Se termina el bucle!")
        break

print("FIN")




