# Bucles [Python]
# Ejemplos de clase

# Autor: Inove Coding School
# Version: 2.0

# Ejemplos de bucles while y buscar el máximo

# Como bien vimos, los bucles while "mientras"
# se deben utilizar cuando no se conoce la secuencia que se recorrerá
# Cuando se posee la secuencia se debe usar el bucle for "para"
# El bucle while se utiliza mucho para hacer que un programa corra/funcione
# indefinidamente hasta que una condición de salida ocurra
# Ejemplificaremos esto junto al uso de un ejercicio con bucle for

# El objetivo es pedir por consola un número y almacenarlo en un listado
# para imprimirlo al final.
# Además, se debe almacenar cual fue el máximo número ingresado
# Se debe repetir este proceso hasta que se ingrese un número negativo
# Solo se aceptan números positivos o cero

maximo_numero = None
lista_numeros = []

while True:
    # Tomamos el valor de la consola
    print("Ingrese un número mayor o igual a cero")
    numero = int(input())

    # Verificamos si el número es negativo
    if numero < 0:
        print('Hasta acá llegamos!')
        break   # Salgo del bucle!

    # Verifico si el número ingresado es mayor al
    # máximo número ingresado hasta el momento
    if (maximo_numero is None) or (numero > maximo_numero):
        maximo_numero = numero

    lista_numeros.append(numero)

# Termino el bucle imprimo la lista de números:
print("Lista: ", lista_numeros)
# Imprimo el máximo número encontrado
print("Máximo número = ", maximo_numero)
# Imprimo el máximo número utilizando la función max de Python
print("Máximo número con Python = ", max(lista_numeros))
# Imprimo el índice del máximo número en la lista
print("Índice del máximo número en la lista = ",
        lista_numeros.index(maximo_numero))
# Imprimo cuantas veces se repite el máximo número en la lista
print("Cantidad del máximo número en la lista = ",
        lista_numeros.count(maximo_numero))

print("terminamos!")
