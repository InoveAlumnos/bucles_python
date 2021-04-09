# Bucles [Python]
# Ejemplos de clase

# Autor: Inove Coding School
# Version: 2.0

# Ejemplo de como contar la cantidad de veces
# que un elemento se repite o evento ocurre

# En este ejemplo se contará cuantas veces se ingresa
# un número par
# El bucle finaliza al ingresar vacio

# primero debo inicializar mi contador
# Como vamos a "contar", el contador debe arrancar en "0"
contador = 0

# Bandera que usamos para indicar que el bucle siga corriendo
numero_valido = True
print("Ingrese cualquier número entero mayor a cero")
print("Ingrese número negativo para teriminar el programa")
while numero_valido:
    numero = int(input())

    if numero >= 0:
        if(numero % 2) == 0:    # El número es par?
            contador += 1       # Incremento el contador
            print("Contador =", contador)
    else:
        numero_valido = False   # Número negativo, numero_valido falso

print("terminamos!")