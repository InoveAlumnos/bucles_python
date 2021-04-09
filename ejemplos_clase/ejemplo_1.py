# Bucles [Python]
# Ejemplos de clase

# Autor: Inove Coding School
# Version: 2.0

# Ejemplos con bucle while "mientras"
x = 0

# En este caso realizaremos un bucle mientras
# x sea menor a 5
while x < 5:
    print('Valor x=', x)
    x +=1   # Incrementar x en 1

# En este caso realizaremos un bucle mientras
# x sea menor a 5
valor_maximo = 5

while x < valor_maximo:
    if x == 4:
        print('Bucle interrumpido en x=', x)
        break

    x_aux = x   # Guardamos en una variable auxiliar (aux) el valor de x
    x += 1      # Incrementamos el valor de x para que el bucle avance

    # Si x es par, continuo el bucle sin terminarlo
    if (x_aux % 2) == 0:
        continue

    # Imprimimos en pantalla el valorde x_aux,
    # que era el valor de x antes de incrementarlo
    print(x_aux, 'es menor a', valor_maximo)

while True:
    print('Ingrese un número distinto de cero!')
    numero = int(input())

    if numero == 0:
        print('Se acabó el juego! numero={}'.format(numero))
        break
    print('Número ingresado={}'.format(numero))

print("terminamos!")