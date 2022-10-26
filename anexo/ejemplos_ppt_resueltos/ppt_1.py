# Bucles [Python]
# Ejemplos de clase

# Autor: Inove Coding School
# Version: 3.0

# Ejemplos con listas

# Variable de tipo texto
# Es 1 invitado, nombre en singular
invitado = "Manuel"

# Variable del tipo lista de textos
# Son muchos invitados, nombre en plural
invitados = ["Manuel", "Ana", "Juan", "Laura"]

# Imprimir la variable invitados
print(invitados)

# Variable del tipo lista, inicia vacia
edades = []

# Podemos agregar las edades de los invitados
# a la lista utilizando el método append (agregar)
edades.append(35)
edades.append(38)
edades.append(55)
edades.append(53)

# Imprimir la variable edades
print(edades)

# Se puede utilizar el operador corchetes
# para acceder a cualquier elemento de una lista

# Acceder a los datos del invitado nº3
invitado_3 = invitados[2]
edad_3 = edades[2]
print(f"La edad de {invitado_3} es {edad_3}")
# La edad de Juan es 55"

# Con la función len podemos ver cuántos elementos
# posee una variable del tipo lista
cantidad_invitados = len(invitados)
print(cantidad_invitados)

# Podemos comparar si ambas listas tiene el mismo
# tamaño
if len(invitados) == len(edades):
    print("¡Listas de igual tamaño!")

print("FIN")



