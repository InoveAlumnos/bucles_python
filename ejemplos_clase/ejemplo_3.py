# Bucles [Python]
# Ejemplos de clase

# Autor: Inove Coding School
# Version: 2.0

# Ejemplo de como contar la cantidad de veces
# que un elemento se repite o evento ocurre

# En este ejemplo se contará cuantas veces se ingresa
# un número par
# El bucle finaliza al ingresar un número negativo

# primero debo inicializar mi contador
# Como vamos a "contar", el contador debe arrancar en "0"
contador = 0

print("Ingrese cualquier número entero mayor a cero")
print("Ingrese número negativo para teriminar el programa")

while True:
    numero = int(input())

    if numero >= 0:
        if(numero % 2) == 0:    # El número es par?
            contador += 1       # Incremento el contador
            print("Contador =", contador)
    else:
        # Terminó el bucle
        print("Número ingresado negativo, termina el bucle")
        break

print("terminamos!")
