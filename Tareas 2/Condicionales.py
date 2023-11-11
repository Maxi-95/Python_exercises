# Ejercicio 1
# Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

# edad = int(input("su edad por favor: "))

# if edad < 18:
#     print("eres menor de edad")
# else:
#     print("eres mayor de edad")

# Ejercicio 2
# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

# contraseña = "ContrAseñA"
# contraseña2 = input("contraseña: ")


# if contraseña2.upper() == contraseña.upper():
#     print("contraseña correcta")
# else:
#     print("contraseña incorrecta")

# Ejercicio 3
# Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.

# numero = int(input("numero a divir: "))
# divisor = int(input("numero divisor: "))

# result = numero // divisor
# if result == 0:
#     print("Error")
# else:
#     print(result)

# Ejercicio 4
# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

# n = int(input("numero: "))
# if n % 2 == 0:
#     print(n, "es par.")
# else:
#     print(n, "es impar")

# Ejercicio 5
# Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

# edad = int(input("edad: "))
# sueldo = int(input("sueldo: "))

# if edad > 16:
#     if sueldo > 1000:
#         print("tiene que tributar")
#     if sueldo < 1000:
#         print("no gana lo suficiente para tributar")
# else:
#     print("todabia es menor para tributar")

# Ejercicio 6
# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
# import string

# nombre = input("alumno/a: ")
# sexo = input("sexo: ")
# alfabeto = list(string.ascii_lowercase)


# for letra in alfabeto:
#     if nombre[0] == letra[0:12]:
#         if sexo == "mujer":
#             print("Grupo ( A )")
#         if sexo == "hombre":
#             print("Grupo ( B )")
#     elif nombre[0] == letra[12:]:
#         if sexo == "hombre":
#             print("Grupo ( A )")
#         if sexo == "mujer":
#             print("Grupo ( B )")


# Ejercicio 7
# Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

# Renta	Tipo impositivo
# Menos de 10000€	5%
# Entre 10000€ y 20000€	15%
# Entre 20000€ y 35000€	20%
# Entre 35000€ y 60000€	30%
# Más de 60000€	45%
# Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.

# Pedir al usuario la renta anual
# renta_anual = float(input("Ingrese su renta anual: "))

# # Determinar el tipo impositivo
# if renta_anual < 10000:
#     tipo_impositivo = 5
# elif 10000 <= renta_anual <= 20000:
#     tipo_impositivo = 15
# elif 20000 < renta_anual <= 35000:
#     tipo_impositivo = 20
# elif 35000 < renta_anual <= 60000:
#     tipo_impositivo = 30
# else:
#     tipo_impositivo = 45

# # Mostrar el resultado
# print(
#     f"Su renta anual es de {renta_anual}€ y su tipo impositivo es del {tipo_impositivo}%.")

# Ejercicio 8
# En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.

# Nivel	Puntuación
# Inaceptable	0.0
# Aceptable	0.4
# Meritorio	0.6 o más
# Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.

# puntuación = float(input("puntuacion del empleado: "))

# if puntuación == 0.0:
#     print("el empleado es Inaceptable")
# elif puntuación == 0.4:
#     print(f"el empleado es Aceptable y recibira {2.400 * 0.4}")
# elif puntuación == 0.6:
#     print(f"el empleado es Meritorio y recibira {2.400 * puntuación}")

# Ejercicio 9
# Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.


# Ejercicio 10
# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

# Ingredientes vegetarianos: Pimiento y tofu.
# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
