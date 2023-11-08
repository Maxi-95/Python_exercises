# Ejercicio 1
# Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

# palabra = input("palabra: ")

# numero = 0

# while numero < 11:
#     print(palabra)
#     numero += 1 

# --------------------------------------------------
# Ejercicio 2
# Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

# edad = int(input("ingrese su edad: "))

# numero = 0
# while numero <= edad:
#     print(numero)
#     numero += 1
    
    
# --------------------------------------------------
# Ejercicio 3
# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

# final = int(input("ingrese un numero: "))

# impares = ",".join(str(num) for num in range(1, final + 1, 2))
# print(impares)

# --------------------------------------------------
# Ejercicio 4
# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

# numero = int(input("ingrese un numero:"))
# serie = []
# num = 0

# while num < numero:
#     numero -= 1
#     serie.append(numero) 
# cadena = ", ".join(map(str, serie))
# print(cadena)

# --------------------------------------------------
# Ejercicio 5
# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

# inversion = int(input("inversion: "))
# interes = float(input("Interés anual (en porcentaje): "))  # Usamos float
# tiempo_en_años = int(input("Cantidad de años: "))

# # Convertir el interés de porcentaje a fracción
# interes = interes / 100.0

# for año in range(tiempo_en_años):
#     # Calcular el capital acumulado utilizando la fórmula del interés compuesto
#     capital_acumulado = inversion * (1 + interes)
#     print(f"Año {año + 1}: {capital_acumulado:.2f}")  # Mostrar el resultado con dos decimales
#     inversion = capital_acumulado
    
# --------------------------------------------------
# Ejercicio 6
# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.

# numero = int(input("ingrese un numero: "))

# inicio = 0

# for num in range(numero):
#     serie = []
#     for _ in range(num):
#         serie.append(_)
    
#     print(serie)    
    
    
# *
# **
# ***
# ****
# *****
# --------------------------------------------------
# Ejercicio 7
# Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

# for _ in range(10):
#     result = _ * 10
#     print(f"{_} * 10: {result}")

# --------------------------------------------------
# Ejercicio 8
# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.

# final = int(input("ingrese un numero: "))


# for num in range(1, final + 1, 2):
#     # for _ in range(num, 0, -2):
#         serie = [_ for _ in range(num, 0, -2)]
        
#         # print(_)
#         print(serie)

# 1
# 3 1
# 5 3 1
# 7 5 3 1
# 9 7 5 3 1
# --------------------------------------------------
# Ejercicio 9
# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

contraseña = "arsovispo"

aprobado = ""

# insistir hasta que se introdusa la contraseña correcta
while aprobado == contraseña:
    la_contraseña = input("contraseña: ")
    aprobado = la_contraseña
    

print("contraseña Correcta")

# --------------------------------------------------
# Ejercicio 10
# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
