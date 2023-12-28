# Ejercicio 1
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.

# materia1 = input("materia 1: ")
# materia2 = input("materia 2: ")
# materia3 = input("materia 3: ")
# materia4 = input("materia 4: ")
# materia5 = input("materia 5: ")

# lista = [materia1, materia2, materia3, materia4, materia5]

# print(lista)

# Ejercicio 2
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.

# asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

# # Muestra las asignaturas por pantalla
# print("Asignaturas del curso:")
# for asignatura in asignaturas:
#     print(f"Yo estudio {asignatura}")

# Ejercicio 3
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.

# asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

# for asignatura in asignaturas:
#     note = input(f"nota de {asignatura}: ")
#     print(f"{asignatura}: {note}")

# Ejercicio 4
# Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

# numeros_ganadores = input("Elija los numeros: ")

# palabras = numeros_ganadores.split()

# # Unir las palabras con comas
# resultado = ", ".join(palabras)


# print(f"Los numeros ganadores son {resultado.sort()}")


# Ejercicio 5
# Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.
# lista = []

# for i in range(1, 11):
#     lista.append(i)
# lista.sort(reverse=True)
# print(lista)

# Ejercicio 6
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.

# asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

# rendir = []

# for asignatura in asignaturas:
#     note = input(f"nota de {asignatura}: ")
#     if note < "6":
#         rendir.append(asignatura)
#     else:
#         print(f"{asignatura}: {note} - Aprobado -")

# print(f"Tiene que rendir: {rendir}")


# Ejercicio 7
# Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.

# abecedario = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]

# lista_resultante = []

# for indice, valor in enumerate(abecedario):
#     if indice % 3 == 0:
#         lista_resultante.append(valor)

# print(lista_resultante)

# Ejercicio 8
# Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.

# palabra = input("escriba la palabra: ")

# result1 = list(palabra)
# result2 = result1[::-1]
# if result1 == result2:
#     print(f"la palabra {palabra} es un palindromo")
# else:
#     print(f"la palabra {palabra} NO es un palindromo")

# Ejercicio 9
# Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.

# # Pedir al usuario una palabra
# palabra = input("Ingresa una palabra: ")

# # Inicializar contadores para cada vocal
# contador_a = contador_e = contador_i = contador_o = contador_u = 0

# # Iterar sobre cada caracter de la palabra
# for letra in palabra:
#     # Convertir la letra a minúscula para hacer la comparación sin importar mayúsculas/minúsculas
#     letra = letra.lower()
    
#     # Verificar si la letra es una vocal y actualizar el contador correspondiente
#     if letra == 'a':
#         contador_a += 1
#     elif letra == 'e':
#         contador_e += 1
#     elif letra == 'i':
#         contador_i += 1
#     elif letra == 'o':
#         contador_o += 1
#     elif letra == 'u':
#         contador_u += 1

# # Mostrar los resultados
# print(f"Número de veces que aparece la vocal 'a': {contador_a}")
# print(f"Número de veces que aparece la vocal 'e': {contador_e}")
# print(f"Número de veces que aparece la vocal 'i': {contador_i}")
# print(f"Número de veces que aparece la vocal 'o': {contador_o}")
# print(f"Número de veces que aparece la vocal 'u': {contador_u}")


# Ejercicio 10
# Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.