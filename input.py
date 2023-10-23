# INPUTS
# Escribí un programa que solicite al usuario ingresar un número con decimales y almacenalo en una variable. A continuación, el programa debe solicitar al usuario que ingrese un número entero y guardarlo en otra variable. En una tercera variable se deberá guardar el resultado de la suma de los dos números ingresados por el usuario. Por último, se debe mostrar en pantalla el texto “El resultado de la suma es [suma]”, donde “[suma]” se reemplazará por el resultado de la operación.

# Primer número: 14.2
# Segundo número: 19
# El resultado de la suma es 33.2

# Solicitar al usuario ingresar un número con decimales
numero_decimal = float(input("Primer número: "))

# Solicitar al usuario ingresar un número entero
numero_entero = int(input("Segundo número: "))

# Calcular la suma de los dos números
resultado = numero_decimal + numero_entero

# Mostrar el resultado en pantalla
print(f"El resultado de la suma es {resultado}")
