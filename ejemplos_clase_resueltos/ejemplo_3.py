# Bucles [Python]
# Ejemplos de clase

# Autor: Inove Coding School
# Version: 3.0

# Ejemplos con bucle for, listas y
# operador incremento (+=)

# Comenzar con una lista de edades
# Objetivo --> sumar todas las edades
# utilizando un bucle y el operador incremento (+=)
edades = [35, 38, 55, 33]

suma_edades = 0

# Profe:
# Utilizar un bucle for sobre la lista de edades
# acumule en la variable "suma_edades" (+=)
# la suma de todas las edades

for edad in edades:
    suma_edades += edad

# Imprimir en pantalla la suma total de edades
print(suma_edades)

# NOTA:
# Más adelante veremos que con la función
# "sum" puede logrese el mismo efecto
# sin utilizar un bucle