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
area = int(input("area: "))


def area_del_circulo(area):
    area = math.pi * radio**2
    return area


# Ejercicio 6
# Escribir una función que reciba una muestra de números en una lista y devuelva su media.


# Ejercicio 7
# Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.


# Ejercicio 8
# Escribir una función que reciba una muestra de números en una lista y devuelva un diccionario con su media, varianza y desviación típica.


# Ejercicio 9
# Escribir una función que calcule el máximo común divisor de dos números y otra que calcule el mínimo común múltiplo.


# Ejercicio 10
# Escribir una función que convierta un número decimal en binario y otra que convierta un número binario en decimal.
