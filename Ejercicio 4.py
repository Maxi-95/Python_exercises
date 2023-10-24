# Escribí un programa que solicite al usuario ingresar la cantidad de kilómetros recorridos por una motocicleta y la cantidad de litros de combustible que consumió durante ese recorrido. Mostrar el consumo de combustible por kilómetro.

# Ejemplo de ejecución:

# Kilómetros recorridos: 260
# Litros de combustible gastados: 12.5
# El consumo por kilómetro es de 20.8

# pedir a usuario ingresar los kilometros
kilometros = int(input("kilometros recorridos: "))
# pedir a usuario ingresar los litros de conbustibles
conbustible = float(input("litros de conbustibles: "))

# dividir los kilometros por la cantidad de litros de conbustibles
resultado = kilometros / conbustible

# mostrar el resultado
print(resultado)
