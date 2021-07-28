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

while True:
    print("Ingrese cualquier número entero mayor o igual a cero")
    print("Ingrese número negativo para teriminar el programa")
    numero = int(input())

    if numero >= 0:
        if(numero % 2) == 0:    # El número es par?
            contador += 1       # Incremento el contador
            print("Contador =", contador)
        else:
            print("Se ha ingresado un número impar, no se aumenta el contador")
    else:
        # Terminó el bucle
        print("Número ingresado negativo, termina el bucle")
        break

print("¿Cuántos números pares ingresó el usuario?", contador)
print("terminamos!")
