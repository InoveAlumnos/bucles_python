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

print('terminó el bucle while')
    
# En este caso realizaremos un bucle mientras
# x sea menor a 5
valor_maximo = 5

# Volvemos a iniciar x en un valor, pero
# para variar x iniciará en 2
x = 2

while x < valor_maximo:
    if x == 4:
        print('Bucle interrumpido en x=', x)
        break

    print('Valor x=', x)
    x += 1      # Incrementamos el valor de x para que el bucle avance


while True:
    print('Ingrese un número distinto de cero!')
    numero = int(input())

    if numero == 0:
        print('Se acabó el juego! numero =', numero)
        break

    print('Número ingresado =', numero)

print("terminamos!")
