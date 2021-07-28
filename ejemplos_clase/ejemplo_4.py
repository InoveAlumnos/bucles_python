# Bucles [Python]
# Ejemplos de clase

# Autor: Inove Coding School
# Version: 2.0

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

print("El valor final de la sumatoria de todos los números es:", sumatoria)
print("terminamos!")
