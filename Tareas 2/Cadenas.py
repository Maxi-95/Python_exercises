# Ejercicio 1
# Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.

# nombre = input("ingresar nombre: ")
# numero = int(input("ingresa un numero: "))

# inicio = 0
# while inicio < repeticiones:
#     print(f"{nombre} dice hola")
#     inicio += 1

# for _ in range(numero):
#     print(nombre)

# --------------------------------------------------
# Ejercicio 2
# Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.

# nombre_completo = input("ingrese el nombre completo: ")
# mayúscula = nombre_completo.upper()
# minuscula = nombre_completo.lower()
# nombre_completo_capitalizado = nombre_completo.title()

# print(mayúscula)
# print(minuscula)
# print(nombre_completo_capitalizado)

# --------------------------------------------------
# Ejercicio 3
# Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.

# nombre = input("ingrese el nombre: ")
# print(f"el nombre {nombre.upper()} tiene {len(nombre)} caracteres")

# --------------------------------------------------
# Ejercicio 4
# Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.

# telefono = input("numero de telefono: ")
# lista = telefono.split()
# numero = lista[1]

# print(f"Tu numero es: {numero}")
# # print(lista)

# --------------------------------------------------
# Ejercicio 5
# Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.

# frase = input("introducir frase: ")

# reversa = frase[::-1]
# print(reversa)

# --------------------------------------------------
# Ejercicio 6
# Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.

# frase = input("frase por favor: ")
# vocal = input("vocal por favor: ")
# lista = list(frase)
# print(lista)

# new_array = []

# for la_vocal in frase:
#     #    if la_vocal == vocal:
#     # vocal = la_vocal.upper()
#     result = la_vocal.replace(vocal, vocal.upper())
#     new_array.append(result)


# s = "".join(new_array)
# print(s)

# --------------------------------------------------
# Ejercicio 7
# Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.

# correo = input("ingrese correo: ")

# nombre = ""

# for letra in correo:
#     nombre += letra
#     if letra == "@":
#         break

# print(f"{nombre}.ceu.es")

# --------------------------------------------------
# Ejercicio 8
# Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido.

# producto = float(input("precio del catalizador: "))
# print(f"el 1lt del catalizador vale:  € ${producto}")
# --------------------------------------------------
# Ejercicio 9
# Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.

# fecha = input("Fecha de nacimiento: ")

# dia = ""
# mes = ""
# año = ""

# for caracter in fecha:
#     if caracter != "/":
#         # Agregar el carácter al valor correspondiente
#         dia += caracter
#     else:
#         # Cambiar a la variable mes después de encontrar "/"
#         mes = dia
#         dia = ""

# # El último valor se almacena en el año
# año = dia

# print(f"""
#       Día: {dia}
#       Mes: {mes}
#       Año: {año}
#       """)


# --------------------------------------------------
# Ejercicio 10
# Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.

# lista_de_compras = input("lista de compras: ")
# lista = lista_de_compras.split(",")

# for producto in lista:
#     print(f"""{producto}""")
