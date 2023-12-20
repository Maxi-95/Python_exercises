import math

# Ejercicio 1
# Escribir una función que muestre por pantalla el saludo ¡Hola amiga! cada vez que se la invoque.

# def saludo():
#     return "Hola amiga!"

# print(saludo())

# Ejercicio 2
# Escribir una función a la que se le pase una cadena <nombre> y muestre por pantalla el saludo ¡hola <nombre>!.

# def saludo(nombre):
#     saludar = "Hola " + nombre
#     return saludar

# result = saludo("maxi")
# print(result)

# Ejercicio 3
# Escribir una función que reciba un número entero positivo y devuelva su factorial.

# def factorial(num):
#     inicio = 0
#     result = 1
#     while inicio < num:
#         inicio += 1
#         result = inicio * result

#     return inicio


# result = factorial(3)
# print(result)


# def factorial(num):
#     # inicio = int(num)
#     result = 1

#     for i in range(1, num + 1, 1):
#         result *= i

#     return result


# resultado = factorial(5)
# print(resultado)

# Ejercicio 4
# Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.

# factura = int(input("factura: "))
# iva = float(input("iva: "))


# def facturacion(factura, iva=None):
#     if iva is None:
#         return factura * 1.21

#     else:
#         return factura * iva


# num = facturacion(factura, iva)
# print(num)

# Ejercicio 5
# Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función.

# area = int(input("area: "))
# altura = int(input("altura: "))

# def calcular_area_circulo(radio):
#     area = math.pi * radio**2
#     return area

# def calcular_volumen_cilindro(altura, area):
#     el_area = calcular_area_circulo(area)
#     volumen = el_area * altura
#     return volumen

# result = calcular_volumen_cilindro(altura, area)
# print(result)

# Ejercicio 6
# Escribir una función que reciba una muestra de números en una lista y devuelva su media.

# lista2 = list(input("introduce una lista: "))
# # lista = [2,3,6,4,7,8,1]

# def longitud(list):
#     return len(list)

# resultado = longitud(lista2)
# print(resultado)

# Ejercicio 7
# Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.

# def calcular_cuadrados(muestra):
#     cuadrados = [numero ** 2 for numero in muestra]
#     return cuadrados

# muestra_numeros = [2, 4, 6, 8, 10]
# cuadrados_resultantes = calcular_cuadrados(muestra_numeros)

# print(f"La muestra original: {muestra_numeros}")
# print(f"Los cuadrados de la muestra: {cuadrados_resultantes}")

# Ejercicio 8
# Escribir una función que reciba una muestra de números en una lista y devuelva un diccionario con su media, varianza y desviación típica.

# lista = [2, 4, 4, 4, 5, 5, 7, 9]

# def diccionario(lista):
#     # media
#     media = sum(lista) / len(lista)

#     # varianza
#     varianza = sum((x - media) ** 2 for x in lista) / len(lista)

#     # desviación típica
#     desviación_típica = math.sqrt(varianza)

#     result = {
#         'Media': media,
#         'Varianza': varianza,
#         'Desvio Tipico': desviación_típica
#     }

#     return result


# result = diccionario(lista)
# print(result)

# Ejercicio 9
# Escribir una función que calcule el máximo común divisor de dos números y otra que calcule el mínimo común múltiplo.

# num1 = int(input("ingrese un numero: "))
# num2 = int(input("ingrese el numero 2: "))


# def result(num1, num2):
#     while num2 != 0:
#         resto = num1 % num2
#         num1 = num2
#         num2 = resto

#     mcd = num1
#     return mcd


# def multi(num1, num2):
#     return abs(num1 * num2) // result(num1, num2)


# resultado = multi(num1, num2)
# print(resultado)

# Ejercicio 10
# Escribir una función que convierta un número decimal en binario y otra que convierta un número binario en decimal.

# decimal = 13


# def decimal_a_binario(decimal):
#     binario = []
#     while decimal != 0:
#         binario.insert(0, decimal % 2)
#         decimal = decimal // 2
#     return binario


# # Llamando a la función para obtener la representación binaria
# binario = decimal_a_binario(decimal)
# cadena_binaria = ''.join(map(str, binario))


# def binario_a_decimal(binario):
#     decimal = 0
#     longitud = len(binario)

#     for i in range(longitud):
#         bit = int(binario[i])
#         exponente = longitud - 1 - i
#         decimal += bit * (2 ** exponente)

#     return decimal


# # Llamando a la función para convertir binario a decimal
# decimal_resultante = binario_a_decimal(binario)

# print(decimal_resultante)

# print(cadena_binaria)
