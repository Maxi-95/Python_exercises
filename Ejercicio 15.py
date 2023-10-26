# Escribí un programa que le pida al usuario ingresar dos palabras y las guarde en dos variables, y que luego imprima True si la primera palabra es menor que la segunda o False si no lo es.
 
# Ejemplo de ejecución:

# Una palabra: complejidad
# Otra palabra: algoritmo
# Falsez


palabra1 = input("ingresa la primera palabra: ")
palabra2 = input("ingresa la segunda palabra: ")

if len(palabra1) < len(palabra2):
    print(True)
    
else:
    print(False)