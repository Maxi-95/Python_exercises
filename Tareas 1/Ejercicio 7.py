# Escribí un programa que solicite al usuario un número y le reste el 15%, almacenando todo en una única variable. A continuación, mostrar el resultado final en pantalla.

# Ejemplo de ejecución:

# Ingresá un número: 260
# Descontando el 15% queda: 221.0

numero = int(input("su numero: "))

resultado = numero * 15 / 100
total = numero - resultado

print(total)