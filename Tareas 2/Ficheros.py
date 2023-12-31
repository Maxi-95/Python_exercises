import urllib.request
import re
# Ejercicio 1
# Escribir una función que pida un número entero entre 1 y 10 y guarde en un fichero con el nombre tabla-n.txt la tabla de multiplicar de ese número, done n es el número introducido.

# with open('tabla-n.txt', 'w') as archivo:
#     archivo.write(input("elija el numero del 1 al 10: "))

# with open('tabla-n.txt', 'r') as archivo:
#     contenido = int(archivo.read())

#     for numero in range(1, contenido + 1):
#         print(f"{numero} * {contenido} = {numero*contenido}")

# def guardar_tabla_multiplicar():
#     # Solicitar al usuario un número entre 1 y 10
#     numero = int(input("Ingrese un número entero entre 1 y 10: "))

#     # Validar que el número esté en el rango especificado
#     if 1 <= numero <= 10:
#         # Generar la tabla de multiplicar y guardarla en un fichero
#         with open(f'tabla-{numero}.txt', 'w') as archivo:
#             for i in range(1, 11):
#                 resultado = numero * i
#                 archivo.write(f"{numero} x {i} = {resultado}\n")
#         print(f"Tabla de multiplicar del {numero} guardada en tabla-{numero}.txt")
#     else:
#         print("El número ingresado no está en el rango permitido.")

# # Llamar a la función
# guardar_tabla_multiplicar()

# def mostrar_tabla_guardada():
#     # Solicitar al usuario el número de la tabla que desea mostrar
#     numero = int(input("Ingrese el número para mostrar la tabla guardada: "))

#     try:
#         # Intentar abrir el archivo correspondiente
#         with open(f'tabla-{numero}.txt', 'r') as archivo:
#             contenido = archivo.read()
#             print(contenido)
#     except FileNotFoundError:
#         print(f"No se encontró la tabla para el número {numero}. Asegúrese de haber guardado la tabla previamente.")

# # Llamar a la función para mostrar la tabla guardada
# mostrar_tabla_guardada()


# Ejercicio 2
# Escribir una función que pida un número entero entre 1 y 10, lea el fichero tabla-n.txt con la tabla de multiplicar de ese número, done n es el número introducido, y la muestre por pantalla. Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.

# def mostrar_tabla_guardada():
#     # Solicitar al usuario el número de la tabla que desea mostrar
#     numero = int(input("Ingrese el número para mostrar la tabla guardada: "))

#     try:
#         # Intentar abrir el archivo correspondiente
#         with open(f'tabla-{numero}.txt', 'r') as archivo:
#             contenido = archivo.read()
#             print(contenido)
#     except FileNotFoundError:
#         print(f"No se encontró la tabla para el número {numero}. Asegúrese de haber guardado la tabla previamente.")

# # Llamar a la función para mostrar la tabla guardada
# mostrar_tabla_guardada()

# Ejercicio 3
# Escribir una función que pida dos números n y m entre 1 y 10, lea el fichero tabla-n.txt con la tabla de multiplicar de ese número, y muestre por pantalla la línea m del fichero. Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.

# def mostrar_tabla_guardada():
#     # Solicitar al usuario el número de la tabla que desea mostrar
#     numero1 = int(input("Ingrese el número para mostrar la tabla guardada: "))
#     numero2 = int(
#         input("Ingrese el número para mostrar una fila de la tabla: "))

#     try:
#         # Intentar abrir el archivo correspondiente
#         with open(f'tabla-{numero1}.txt', 'r') as archivo:
#             contenido = archivo.read()
#             lista2 = contenido.split("\n")
#             for i in range(len(lista2)):
#                 if i == numero2:
#                     print(lista2[i])
#     except FileNotFoundError:
#         print(
#             f"No se encontró la tabla para el número {numero}. Asegúrese de haber guardado la tabla previamente.")


# Llamar a la función para mostrar la tabla guardada
# mostrar_tabla_guardada()

# Ejercicio 4
# Escribir un programa que acceda a un fichero de internet mediante su url y muestre por pantalla el número de palabras que contiene.

# url = "https://jsonplaceholder.typicode.com/posts/1"

# try:
#     # Abrir la conexión y leer el contenido del archivo
#     with urllib.request.urlopen(url) as response:
#         contenido = response.read().decode('utf-8')
#         lista = len(contenido.split())

#         print(lista)
# except Exception as e:
#     print(f"Error al acceder a la URL: {e}")


# Ejercicio 5
# Escribir un programa que abra el fichero con información sobre el PIB per cápita de los países de la Unión Europea (url:https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true), pregunte por las iniciales de un país y muestre el PIB per cápita de ese país de todos los años disponibles.


# Ejercicio 6
# Escribir un programa para gestionar un listín telefónico con los nombres y los teléfonos de los clientes de una empresa. El programa incorporar funciones crear el fichero con el listín si no existe, para consultar el teléfono de un cliente, añadir el teléfono de un nuevo cliente y eliminar el teléfono de un cliente. El listín debe estar guardado en el fichero de texto listin.txt donde el nombre del cliente y su teléfono deben aparecer separados por comas y cada cliente en una línea distinta.


# Ejercicio 7
# El fichero cotizacion.csv contiene las cotizaciones de las empresas del IBEX35 con las siguientes columnas: Nombre (nombre de la empresa), Final (precio de la acción al cierre de bolsa), Máximo (precio máximo de la acción durante la jornada), Mínimo (precio mínimo de la acción durante la jornada), Volumen (Volumen al cierre de bolsa), Efectivo (capitalización al cierre en miles de euros).

# Construir una función reciba el fichero de cotizaciones y devuelva un diccionario con los datos del fichero por columnas.

# Construir una función que reciba el diccionario devuelto por la función anterior y cree un fichero en formato csv con el mínimo, el máximo y la media de dada columna.


# Ejercicio 8
# El fichero calificaciones.csv contiene las calificaciones de un curso. Durante el curso se realizaron dos exámenes parciales de teoría y un examen de prácticas. Los alumnos que tuvieron menos de 4 en alguno de estos exámenes pudieron repetirlo en la al final del curso (convocatoria ordinaria). Escribir un programa que contenga las siguientes funciones:

# Una función que reciba el fichero de calificaciones y devuelva una lista de diccionarios, donde cada diccionario contiene la información de los exámenes y la asistencia de un alumno. La lista tiene que estar ordenada por apellidos.

# Una función que reciba una lista de diccionarios como la que devuelve la función anterior y añada a cada diccionario un nuevo par con la nota final del curso. El peso de cada parcial de teoría en la nota final es de un 30% mientras que el peso del examen de prácticas es de un 40%.

# Una función que reciba una lista de diccionarios como la que devuelve la función anterior y devuelva dos listas, una con los alumnos aprobados y otra con los alumnos suspensos. Para aprobar el curso, la asistencia tiene que ser mayor o igual que el 75%, la nota de los exámenes parciales y de prácticas mayor o igual que 4 y la nota final mayor o igual que 5.
