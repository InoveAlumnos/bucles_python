#!/usr/bin/env python
'''
Bucles [Python]
Ejemplos de clase
---------------------------
Autor: Inove Coding School
Version: 1.2

Descripcion:
Programa creado para mostrar ejemplos prácticos de los visto durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.2"

valor_maximo = 5


def bucle_while():
    # Ejemplos con bucle while "mientras"
    x = 0

    # En este caso realizaremos un bucle mientras
    # x sea menor a 5
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


def bucle_for():
    # Ejemplos con bucle for "para"

    # Realizaremos el mismo caso que el primer ejemplo de "while"
    # pero ahora con el bucle "for"
    # Este bucle "for" caso es el indicado para este tipo de acciones
    for x in range(valor_maximo):
        if x == 4:
            print('Bucle interrumpido en x=', x)
            break

        # Si x es par, continuo el bucle sin terminarlo
        if (x % 2) == 0:
            continue

        print(x, 'es menor a', valor_maximo)

    # Ahora recorreremos (iterar) una lista de datos en donde
    # en los índices pares (0, 2, 4) se encuentran los nombres de los contactos
    # y en los índices impares (1, 3, 5) los números de los contacto
    # Es una lista mezclada de strings y números
    agenda = ['Claudia', 123, 'Roberto', 456, 'Inove', 789]
    agenda_len = len(agenda)

    for i in range(agenda_len):
        if (i % 2) == 0:
            # Índice par, imprimo nombre
            nombre = agenda[i]
            print("Nombre contacto:", nombre)
        else:
            # Índice impar, imprimo número
            numero = agenda[i]
            print("Número contacto:", numero)


def contador():
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


def sumatoria():
    # Ejemplos de ecuaciones con bucles

    # Cuando queremos realizar la suma de una serie de números
    # la ecuación la escribiriamos de la siguiente forma:
    # sumatoria = numero_1 + numero_2 + numero_3 + .... + numero_10

    # Que es equivalente a hacer un incremento de la variable sumatoria
    # por cada valor deseado a sumar
    # sumatoria += numero_1
    # sumatoria += numero_2
    # sumatoria += numero_3
    # sumatoria += .....
    # sumatoria += numero_10

    # Esta operación se puede realizar con un bucle "for"
    # dado la lista de números
    numeros = [1, 2, 3, 4, 5]

    # Debo primero inicializar la variable donde almacenaré la sumatoria
    # Ya que es necesario que empiece con un valor conocido
    sumatoria = 0

    for numero in numeros:
        sumatoria += numero     # sumatoria = sumatoria + numero
        print("número = ", numero, "sumatoria =", sumatoria)


def buscar_max():
    # Ejemplos de bucles while

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

    print("Ingrese un número mayor o igual a cero")
    while True:
        # Tomamos el valor de la consola
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

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    bucle_while()
    bucle_for()
    contador()
    sumatoria()
    buscar_max()
