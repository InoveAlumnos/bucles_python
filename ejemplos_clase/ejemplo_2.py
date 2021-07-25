# Bucles [Python]
# Ejemplos de clase

# Autor: Inove Coding School
# Version: 2.0

# Ejemplos con bucle for "para"

# Realizaremos el mismo caso que el primer ejemplo de "while"
# pero ahora con el bucle "for"
# Este bucle "for" caso es el indicado para este tipo de acciones
valor_maximo = 5

for x in range(valor_maximo):
    print('Valor x=', x)

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

print("terminamos!")
