# Escribí un programa que solicite al usuario el ingreso de un texto y almacene ese texto en una variable. A continuación, mostrar en pantalla la primera letra del texto ingresado. Luego, solicitar al usuario que ingrese un número positivo menor a la cantidad de caracteres que tiene el texto que ingresó (por ejemplo, si escribió la palabra “HOLA”, tendrá que ser un número entre 0 y 4) y almacenar este número en una variable llamada indice.
# Mostrar en pantalla el carácter del texto ubicado en la posición dada por indice.

# Ejemplo de ejecución:

# Ingresá un texto: En un lugar de La Mancha, de cuyo nombre no quiero acordarme…
# El carácter en primer lugar es: E
# Ingresá un número positivo menor a 63
# 7
# El carácter en esa posición es: u

# Código de ejemplo

# a=10
# b=4
# print(a != b)

# La instrucción print imprimirá True, ya que el valor contenido en a es diferente del valor contenido en b.


texto = input("ingresá un texto: ")

primer_caracter = texto[0]
print(primer_caracter)


numero = int(input("ingresá un numero: "))

if numero < len(texto):
    print(texto[numero])
else:
    print("ingrese un numero menor a la cantidad de caracteres que tiene el texto")