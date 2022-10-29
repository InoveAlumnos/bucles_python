# Bucles [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 3.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos con listas y bucles for

# Objetivo:
# Dado una lista de números, utilizar "for"
# para recorrer toda la lista y realizar 
# la sumatoria de todos los números positivos

# Alumno:
# Usted ya cuenta con la lista numeros
# Crear una variable llamada suma_total
# inicializada en cero
# Realiza un bucle que recorra cada elemento
# En cada iteración incrementar el valor de suma_total
# (con el operador incremento) con cada número positivo
# Utilice un condicional para evaluar si el número
# es positivo

# TIP
# Utilice el debugger para ver como avanza
# el programa paso a paso
numeros = [1, 5, -1, 6, 10, 2, -5]

suma_total = 0
for numero in numeros:
    if numero > 0:
        suma_total += numero

# Imprimir en pantalla la variable temperaturas
# El resultado final de la suma deberá ser 24
print(suma_total)
