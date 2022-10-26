# Bucles [Python]
# Ejemplos de clase

# Autor: Inove Coding School
# Version: 3.0

# Ejemplos con bucle while

# Objetivo:
# Realizar un bucle while infinito
# que finalice (break) cuando se
# ingrese correctamente lo solicitado
# en consola

while True:
    entrada = input("Ingrese la palabra PYTHON:\n")
    entrada = entrada.lower()

    if entrada == "python":
        print("¡Muchas gracias!, termina el bucle")
        break

    print("Palabra ingresada incorrecta, vuelva a intentar")

print("Valor ingresado en el bucle:", entrada)
print("FIN")


