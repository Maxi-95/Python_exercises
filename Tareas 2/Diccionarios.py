# Ejercicio 1
# Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
# consulta = input("existe esta moneda?: ")
# monedas = {
#     'Euro':'€',
#     'Dollar':'$',
#     'Yen':'¥'
#     }

# for clave, valor in monedas.items():
#     if consulta == clave:
#         print(valor)
#     else:
#         print("la moneda no existe en el diccionario")
#         break


# Ejercicio 2
# Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.

# nombre = input("nombre: ")
# edad = input("edad: ")
# direccion = input("direccion: ")
# telefono = input("telefono: ")

# obj = {"nombre": nombre, "edad": edad,
#        "direccion": direccion, "telefono": telefono}

# print(f"{nombre} tiene {edad} años, vive en {direccion} y su número de teléfono es {telefono}")

# Ejercicio 3
# Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

# Fruta	Precio
# Plátano	1.35
# Manzana	0.80
# Pera	0.85
# Naranja	0.70

# Crear un diccionario con los precios de las frutas
# precios_frutas = {"Plátano": 1.35,
#                   "Manzana": 0.80, "Pera": 0.85, "Naranja": 0.70}

# # Solicitar al usuario la fruta y la cantidad de kilos
# fruta = input("Ingrese una fruta: ")
# kilos = float(input("Ingrese la cantidad de kilos: "))

# # Verificar si la fruta está en el diccionario
# if fruta in precios_frutas:
#     precio_por_kilo = precios_frutas[fruta]
#     costo_total = precio_por_kilo * kilos
#     print(f"El precio de {kilos} kilos de {fruta} es: {costo_total}€")
# else:
#     print(f"Lo siento, la fruta {fruta} no está en el diccionario de precios.")


# Ejercicio 4
# Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.

# fecha = input("fecha: ")

# año = {
#     "01": "enero",
#     "02": "febrero",
#     "03": "marzo",
#     "04": "abril",
#     "05": "mayo",
#     "06": "junio",
#     "07": "julio",
#     "08": "agosto",
#     "09": "septiembre",
#     "10": "octubre",
#     "11": "noviemrbre",
#     "12": "diciembre",
# }


# for mes in año:
#     if fecha[3]+fecha[4] == mes:
#         print(f"{fecha[0]+fecha[1]} de {año.get(mes)} de {fecha[6:]}")

# Ejercicio 5
# Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso.

# Almacenar el diccionario con los créditos de las asignaturas
# creditos_asignaturas = {'Matemáticas': 6, 'Física': 4, 'Química': 5}

# # Mostrar los créditos de cada asignatura
# total_creditos = 0  # Inicializar el total de créditos

# for asignatura, creditos in creditos_asignaturas.items():
#     print(f"{asignatura} tiene {creditos} créditos")
#     total_creditos += creditos  # Sumar los créditos al total

# # Mostrar el número total de créditos del curso
# print(f"El número total de créditos del curso es: {total_creditos}")

# Ejercicio 6
# Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
# def usuario(nombre, edad, sexo, telefono):
#     persona = {
#         "nombre": nombre,
#         "edad": edad,
#         "sexo": sexo,
#         "telefono": telefono
#     }
#     for clave in persona:
#         print(persona[clave])


# nombre = input("nombre: ")
# usuario(nombre, "", "", "")
# edad = input("edad: ")
# usuario(nombre, edad, "", "")
# sexo = input("sexo: ")
# usuario(nombre, edad, sexo, "")
# telefono = input("telefono: ")
# usuario(nombre, edad, sexo, telefono)

# Crear un diccionario vacío
# persona = {}

# while True:
#     # Solicitar información al usuario
#     campo = input(
#         "Ingrese un campo (nombre, edad, sexo, teléfono, correo electrónico) o 'salir' para finalizar: ")

#     if campo.lower() == 'salir':
#         break  # Salir del bucle si el usuario ingresa 'salir'

#     valor = input(f"Ingrese el valor para '{campo}': ")

#     # Almacenar la información en el diccionario
#     persona[campo] = valor

#     # Imprimir el contenido actual del diccionario
#     print("Información actual de la persona:")
#     for clave, valor in persona.items():
#         print(f"{clave}: {valor}")


# Ejercicio 7
# Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato

# Lista de la compra
# Artículo 1	Precio
# Artículo 2	Precio
# Artículo 3	Precio
# …	…
# Total	Coste
# Crear un diccionario para la lista de la compra
# cesta_de_la_compra = {}

# while True:
#     # Solicitar al usuario el artículo y su precio
#     articulo = input(
#         "Ingrese el nombre del artículo (o 'terminar' para finalizar): ")

#     if articulo.lower() == 'terminar':
#         break  # Salir del bucle si el usuario ingresa 'terminar'

#     precio = float(input("Ingrese el precio del artículo: "))

#     # Agregar el artículo y su precio al diccionario
#     cesta_de_la_compra[articulo] = precio

# # Imprimir la lista de la compra y el coste total
# print("Lista de la compra")
# total = 0  # Inicializar el coste total

# for articulo, precio in cesta_de_la_compra.items():
#     print(f"{articulo}\t{precio}€")
#     total += precio

# print("Total\tCoste:", total, "€")


# Ejercicio 8
# Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas. El programa debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.

# diccionario = {}
# palabras = input(
#     "Ingrese palabras en español e inglés (separadas por dos puntos, pares separados por comas): ")

# # Separar las palabras y construir el diccionario
# pares = palabras.split(",")
# for par in pares:
#     espanol, ingles = par.split(":")
#     diccionario[espanol.strip()] = ingles.strip()

# # Pedir una frase en español para traducir
# frase_espanol = input("Ingrese una frase en español: ")

# # Traducir la frase palabra por palabra
# palabras_frase = frase_espanol.split()
# traduccion = [diccionario[palabra]
#               if palabra in diccionario else palabra for palabra in palabras_frase]

# # Mostrar la traducción
# print("Traducción al inglés:", " ".join(traduccion))

# Ejercicio 9
# Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura. El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar. Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario. Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.


# Ejercicio 10
# Escribir un programa que permita gestionar la base de datos de clientes de una empresa. Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF, y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente), donde preferente tendrá el valor True si se trata de un cliente preferente. El programa debe preguntar al usuario por una opción del siguiente menú: (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar. En función de la opción elegida el programa tendrá que hacer lo siguiente:

# Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
# Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
# Preguntar por el NIF del cliente y mostrar sus datos.
# Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
# Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
# Terminar el programa.
