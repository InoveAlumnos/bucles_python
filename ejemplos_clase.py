#!/usr/bin/env python
'''
Condicionales [Python]
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


def numbers():
    # Ejemplos varialbles numéricas
    x = 5
    y = 2

    # Verificar si "x" es par
    if (x % 2) == 0:
        print('x es par')
    else:
        print('x es impar')

    # Verificar si "x" es mayor a "y"
    if x > y:
        print('x =', x, 'es mayor a y =', y)
    else:
        print('y =', y, 'es mayor a x =', x)

    # Realizar la misma operación negando la condición
    if not(x > y):
        print('x={} no es mayor a y={}'.format(x, y))  # Debo también negar la respuesta
    else:
        print('y={} no es mayor a x={}'.format(y, x))  # Debo también negar la respuesta

    # Verificar si "y" es nu número positivo
    if y > 0:
        print('y es positivo')
    elif y < 0:
        print('y es negativo')
    else:
        print('y es 0')

    # Operadores de comparación
    copia_x = x

    if x == copia_x:
        print('x es igual a copia_x')

    if y != copia_x:
        print('y es distinto a copia_x')

    # Condicionales compuestos
    # Calcular el producto entre dos números enteros que sean positivos
    # y menores a 100
    numero_1 = 10
    numero_2 = 30

    if (numero_1 > 0 and numero_1 < 100 and
        numero_2 > 0 and numero_2 < 100):
        producto = numero_1 * numero_2
        print('El producto entre {} y {} es {}'.format(numero_1,
                                                       numero_2,
                                                       producto))

    # Calcular la suma de dos números si almenos uno de ellos
    # es mayor o igual a cero
    numero_3 = -20

    if (numero_1 >= 0) or (numero_3 >= 0):
        suma = numero_1 + numero_3
        print('La suma entre {} y {} es {}'.format(numero_1, numero_3, suma))


def strings():
    # Ejemplos varialbles de texto
    texto_1 = 'a'
    texto_2 = 'b'

    # Verificar que texto es mayores (alfabéticamente)
    if texto_1 > texto_2:
        print('{} es mayor que {}'.format(texto_1, texto_2))
    else:
        print('{} es mayor que {}'.format(texto_2, texto_1))

    texto_1 = 'ab'
    texto_2 = 'aab'

    if texto_1 > texto_2:
        print('{} es mayor que {}'.format(texto_1, texto_2))
    else:
        print('{} es mayor que {}'.format(texto_2, texto_1))

    if texto_1 == 'ab':
        print('texto_1({}) es igual a ab'.format(texto_1))

    # Condicionales compuestos
    # Si texto_1 es mayor a texto_2 e igual a "hola" o
    # texto_1 tiene menos de 4 letras, entonces imprimir "Correcto!"

    if (((texto_1 > texto_2) and texto_1 == 'hola') or
       (len(texto_1) < 4)):
       print('Correcto!')

if __name__ == '__main__':
    print('Bienvenidos a otra clase de Inove con Python')
    numbers()
    strings()
