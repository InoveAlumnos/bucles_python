# Bucles [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 3.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con listas y bucles
'''
Enunciado:
- Realizar un programa que determine cuantos
  examenes presentó un alumno y cuantos
  ausentes tuvo.
- Las notas negativas dentro de la lista
  son los ausentes, las notas positivas
  son los resultados de los examanes a los
  que se presentó.
- Ya cuenta con la variable notas

Alumno:
- Crear una una variable llamada cantidad_examanes
  para almacenar a cuantos exámenes se presentó
  el alumno (debe inicializarla en cero).
  Utilice un bucle e incremente en 1 la variable
  cantidad_examanes en cada iteración donde la nota
  sea positiva o cero.

- Crear una una variable llamada cantidad_ausentes
  para almacenar la cantidad de ausentes del
  alumno (debe inicializarla en cero).
  Utilice un bucle e incremente en 1 la variable
  cantidad_ausentes en cada iteración donde la nota
  sea negativa.

- BONUS: Todo el ejercicio se puede resolver
  en un único bucle, puede hacer dos bucles
  por separado y luego ver como unirlos en uno solo

- Al final imprimir en pantalla todas las variables
'''

print("Mi organizador académico (#_#)")
# Empezar aquí la resolución del ejercicio
notas = [70, 82, -1, 65, 55, 67, 87, 92, -1]
