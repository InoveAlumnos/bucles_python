#!/usr/bin/env python
'''
Bucles [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

# Variable global utilizada para el ejercicio de nota
notas = [70, 82, -1, 65, 55, 67, 87, 92, -1]

# Variable global utilizada para el ejercicio de temperaturas
temp_dataloger = [12.8, 18.6, 14.5, 20.8, 12.1, 21.2, 13.5, 18.6,
                  14.7, 19.6, 11.2, 18.4]


def ej1():
    print('Comenzamos a ponernos serios!')

    '''
    Realice un programa que pida por consola dos números que representen
    el principio y fin de una secuencia numérica.
    Realizar un bucle "for" que recorra esa secuencia armada con "range"
    y cuente cuantos números ingresados hay, y la sumatoria de todos los números
    Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
    sino que va hasta el anterior
    '''
    inicio = int(input("Ingrese el primer numero de la secuencia\n"))
    ultimo = int(input("Ingrese el ultimo numero de la secuencia\n"))

    cantidad_numero = 0
    sumatoria = 0
    # cantidad_numeros ....
    # sumatoria ....

    # Inove: Un comentario respecot a cantidad_numero, como
    # la cantidad de números no varía se puede calcular
    # una sola vez antes de empezar el bucle o al terminarlo:
    # cantidad_numero = ultimo - inicio
    # Es solo un comentario al pasar, queramos que pruebes
    # el mecanismo de pull-request
    
    for i in range(inicio, ultimo + 1):
        cantidad_numero = ultimo - inicio
        sumatoria += i
    print("La secuencia tiene {} numeros dentro".format(cantidad_numero))
    print("La suma de los numeros dentro de la secuencia es:", sumatoria)

    promedio = sumatoria / cantidad_numero
    print("El promedio de los numeros en la secuencia es:", promedio)

    # Al terminar el bucle calcular el promedio como:
    # promedio = sumatoria / cantidad_numeros

    # Imprimir resultado en pantalla


def ej2():
    print("Mi Calculadora (^_^)")

    '''
    Tome el ejercicio de clase:
    <condicionales_python /  ejercicios_practica / ej3>,
    copielo a este ejercicio y modifíquelo, ahora se deberá ejecutar
    indefinidamente hasta que como operador se ingrese la palabra "FIN",
    en ese momento debe terminar el programa

    Se debe debe imprimir un cartel de error si el operador ingresado no es
    alguno de lo soportados o no es la palabra "FIN"
    '''

    while True:

        print("Ingrese dos numeros:")
        calc_1 = float(input())
        calc_2 = float(input())

        print("Ingrese el simbolo de la operacion que quiere realizar con estos dos numeros:")
        operacion = str(input())

        if operacion == "+":
            print("El resultado de sumar {} con {} es {}".format(calc_1,calc_2, calc_1 + calc_2))
        elif operacion == "-":
            print("El resultado de restar {} con {} es {}".format(calc_1,calc_2, calc_1 - calc_2))
        elif operacion == "*":
            print("El resultado de multiplicar {} con {} es {}".format(calc_1,calc_2, calc_1 * calc_2))
        elif operacion == "/":
            print("El resultado de dividir {} con {} es {}".format(calc_1,calc_2, calc_1 / calc_2))
        elif operacion == "**":
            print("{} elevado a la potencia {} es {}".format(calc_1,calc_2, calc_1 ** calc_2))
        elif operacion == "fin":
            break
        else:
            print("El simbolo ingresado no corresponde a una operacion matematica")
        

def ej3():
    print("Mi organizador académico (#_#)")

    '''
    Tome el ejercicio de "calificaciones":
    <condicionales_python / ejercicios_clase / ej3>,
    copielo a este ejercicio y modifíquelo para cumplir
    el siguiente requerimiento

    Las notas del estudinte se encuentran almacenadas en una
    lista llamada "notas" que ya hemos definido al comienzo del archivo

    Debe calcular el promedio de todas las notas y luego transformar
    la califiación en una letra según la escala establecida en el ejercicio
    "calificaciones" <condicionales_python / ejercicios_clase / ej3>

    A medida que recorre las notas, no debe considerar como válidas aquellas
    que son negativas, en ese caso el alumno estuvo ausente

    Debe contar la cantidad de notas válidas y la cantidad de ausentes
    '''

    # Verifique la calificación de un estudiante según su
    # puntaje en un examen


    # Para calcular el promedio primero debe obtener la suma
    # de todas las notas, que irá almacenando en esta variable
    sumatoria = 0           # Ya le hemos inicializado en 0

    cantidad_notas = 0      # Aquí debe contar cuantas notas válidas encontró
    cantidad_ausentes = 0   # Aquí debe contar cuantos ausentes hubo

    # Realice aquí el bucle para recorrer todas las notas
    # y cacular la sumatoria

    for nota in notas:
        if nota > 0:
            cantidad_notas += 1
            sumatoria += nota
        else:
            cantidad_ausentes += 1

    # Terminado el bucle calcule el promedio como
    # promedio = sumatoria / cantidad_notas

    promedio = sumatoria / cantidad_notas
    print("La nota promedio fue:", promedio)
    # Utilice la nota promedio calculada y transformela
    # a calificación con letras, imprima en pantalla el resultado

    if promedio >= 90:
        print("Tu calificacion es una A")
    elif promedio >= 80:
        print("Tu calificacion es una B")
    elif promedio >= 70:
        print("Tu calificacion es una C")
    elif promedio >= 60:
        print("Tu calificacion es una D")
    elif promedio <= 60:
        print("Tu calificacion es una F")

    # Imprima en pantalla al cantidad de ausentes
    print("La cantidad de ausentes fue", cantidad_ausentes)

def ej4():
    print("Mi primer pasito en data analytics")

    '''
    Tome el ejercicio:
    <condicionales_python / ejercicios_practica /ej5>,
    copielo a este ejercicio y modifíquelo para cumplir el
    siguiente requerimiento

    En este ejercicio se lo provee de una lista de temperatuas,
    esa lista de temperatuas corresponde a los valores de temperaturas
    tomados durante una temperorada del año en Buenos Aires.
    Ustede deberá analizar dicha lista para deducir
    en que temporada del año se realizó el muestreo de temperatura.
    La variable con la lista de temperaturas se llama "temp_dataloger"
    definida al comienzo del archivo

    Debe recorrer la lista "temp_dataloger" y obtener los siguientes
    resultados

    1 - Obtener la máxima temperatura
    2 - Obtener la mínima temperatura
    3 - Obtener el promedio de las temperatuas

    Los resultados se deberán almacenar en las siguientes variables
    que ya hemos preparado para usted.

    NOTA: No se debe ordenar la lista de temperaturas, se debe obtener
    el máximo y el mínimo utilizando los mismos métodos vistos
    durante la clase (ejemplos_clase)
    '''
    print("Las temperaturas son C°:", temp_dataloger)
    temperatura_max = None      # Aquí debe ir almacenando la temp máxima
    temperatura_min = None      # Aquí debe ir almacenando la temp mínima
    temperatura_sumatoria = 0   # Aquí debe ir almacenando la suma de todas las temp
    temperatura_promedio = 0    # Al finalizar el loop deberá aquí alamcenar el promedio
    temperatura_len = 0         # Aquí debe almacenar cuantas temperatuas hay en la lista

    # Colocar el bucle aqui......

    for i in range(len(temp_dataloger)):
        if temperatura_min == None or temp_dataloger[i] < temperatura_min:
            temperatura_min = temp_dataloger[i]
        elif temperatura_max == None or temp_dataloger[i] > temperatura_max:
            temperatura_max = temp_dataloger[i]
        temperatura_sumatoria += temp_dataloger[i]
        temperatura_len += 1
    print("Temperatura maxima:", temperatura_max)
    print("Temperatura minima:", temperatura_min)

    temperatura_promedio = temperatura_sumatoria / temperatura_len
    print("Temperatura promedio:", temperatura_promedio)

    # Al finalizar el bucle compare si el valor que usted calculó para
    # temperatura_max y temperatura_min coincide con el que podría calcular
    # usando la función "max" y la función "min" de python
    # función "max" --> https://www.w3schools.com/python/ref_func_max.asp
    # función "min" --> https://www.w3schools.com/python/ref_func_min.asp

    print("Temperatura maxima usando funcion max: {}".format(max(temp_dataloger)))
    print("Temperatura minima usando funcion min: {}".format(min(temp_dataloger)))
    print("Sumatoria de las temperaturas {}".format(temperatura_sumatoria))
    print("Sumatorias de las temperaturas usando la funcion sum {}".format(sum(temp_dataloger)))
    # Al finalizar el bucle debe calcular el promedio como:
    # temperatura_promedio = temperatura_sumatoria / cantidad_temperatuas

    # Corroboren los resultados de temperatura_sumatoria
    # usando la función "sum"
    # función "sum" --> https://www.w3schools.com/python/ref_func_sum.asp

    '''
    Una vez que tengamos nuestros valores correctamente calculados debemos
    determinar en que epoca del año nos encontramos en Buenos Aires utilizando
    la estadística de años anteriores. Basados en el siguiente link realizamos
    las siguientes aproximaciones:

    verano -->      min = 19, max = 28
    otoño -->       min = 11, max = 24
    invierno -->    min = 8, max = 14
    primavera -->   min = 10, max = 24

    Referencia:
    https://es.weatherspark.com/y/28981/Clima-promedio-en-Buenos-Aires-Argentina-durante-todo-el-a%C3%B1o
    '''
    if temperatura_min > 19 and temperatura_max < 28:
        print("Estamos en verano")
    elif temperatura_min > 11 and temperatura_max < 24:
        print("Estamos en otoño")
    elif temperatura_min > 8 and temperatura_max < 14:
        print("Estamos en invierno")
    elif temperatura_min > 10 and temperatura_max < 24:
        print("Estamos en primavera")

    # En base a los rangos de temperatura de cada estación,
    # ¿En qué época del año nos encontramos?
    # Imprima el resultado en pantalla
    # Debe utilizar temperatura_max y temperatura_min para definirlo


def ej5():
    print("Ahora sí! buena suerte :)")

    '''
    Tome el ejercicio:
    <condicionales_python / ejercicios_practica / ej4>,
    copielo a este ejercicio y modifíquelo para cumplir
    el siguiente requerimiento

    Realize un programa que corra indefinidamente en un bucle, al comienzo de la
    iteración del bucle el programa consultará al usuario con el siguiente menú:
    1 - Ordenar por orden alfabético (usando el operador ">")
    2 - Ordenar por cantidad de letras (longitud de la palabra)
    3 - Salir del programa

    En caso de presionar "3" el programa debe terminar e informar por
    pantalla de que ha acabado,
    en caso contrario si se presionar "1" o "2" debe continuar con la siguiente tarea

    NOTA: Si se ingresa otro valor que no sea 1, 2 o 3 se debe enviar
    un mensaje de error y volver a comenzar el bucle
    (vea en el apunte "Bucles - Sentencias" para encontrar
    la sentencia que lo ayude a cumplir esa tarea)

    Si el bucle continua (se presionó "1" o "2") se debe ingresar a otro bucle
    en donde en cada iteración se pedirá una palabra. La cantidad de iteración
    (cantidad de palabras a solicitar) lo dejamos a gusto del alumno, intente que esa
    condición esté dada por una variable (ej: palabras_deseadas = 4)
    Cada palabra ingresada se debe ir almacenando en una lista de palabras, dicha
    lista la debe inicializar vacia y agregar cada nuevo valor con el método "append".
    Luego de tener las palabras deseadas almacenadas en una lista de palabras
    se debe proceder a realizar las siguientes tareas:

    Si se ingresa "1" por consola se debe obtener la palabra
    más grande por orden alfabético
    Luego de terminar de recorrer toda la lista (utilizar un bucle "for")
    se debe imprimir en pantalla cual era la palabra
    más grande alfabeticamente.
    Recuerde que debe inicializar primero su variable
    donde irá almacenando la palabra que cumpla dicha condición.
    ¿Con qué valor debería ser inicializada dicha variable?

    Si se ingresa "2" por consola se debe obtener la palabra
    con mayor cantidad de letras
    Luego de terminar de recorrer toda la lista (utilizar un bucle "for")
    se debe imprimir en pantalla cual era la palabra con
    mayor cantidad de letras.
    Recuerde que debe inicializar primero su variable
    donde irá almacenando la palabra que cumpla dicha condición.
    ¿Con qué valor debería ser inicializada dicha variable?

    NOTA: No se debe ordenar la lista de palabras, se debe obtener
    el máximo utilizando el mismos métodos vistos durante la clase
    (ejemplos_clase), tal como el ejercicio anterior. Ordenar una
    lista representa un problema mucho más complejo que solo
    buscar el máximo.

    NOTA: Es recomendable que se organice con lápiz y papel para
    hacer un bosquejo del sistema ya que deberá utilizar 3 bucles en total,
    1 - El bucle principal que hace que el programa corra hasta ingresar un "3"
    2 - Un bucle interno que corre hasta socilitar todas las palabras deseadas
        que se deben ir guardando en una lista
    3- Otro bucle interno que corre luego de que termine el bucle "2" que
       recorre la lista de palabras y busca la mayor según el motivo ingresado ("1" o "2")

    '''

    palabras = []

    while True:
        ordenar = int(input("Escriba como desea ordenar las palabras: \n 1) Alfabeticamente \n 2) Cantidad de letras \n 3) Terminar \n"))

        if ordenar == 1 or ordenar == 2:
            palabras_deseadas = int(input("Ingrese la cantidad de palabras que desea ordenar:"))
            if ordenar == 1:    
                for i in range(palabras_deseadas):
                    palabra = str(input("Ingrese una palabra: "))
                    palabras.append(palabra)
                palabra_mayor = None
                for n in palabras:
                    if n == palabras[0] or n > palabra_mayor:
                        palabra_mayor = n
                print("Alfabeticamente la mayor palabra es:", palabra_mayor)
            elif ordenar == 2:
                for i in range(palabras_deseadas):
                    palabra = str(input("Ingrese una palabra: "))
                    palabras.append(palabra)
                palabra_mayor = None
                for n in palabras:
                    if n == palabras[0] or len(n) > len(palabra_mayor):
                        palabra_mayor = n
                print("La mayor palabra por cantidad de letras es:", palabra_mayor)
        elif ordenar == 3:
            break
        else:
            print("El numero solicitado no esta permitido")


if __name__ == '__main__':
    print("Ejercicios de práctica")
    ej1()
    ej2()
    ej3()
    ej4()
    ej5()
