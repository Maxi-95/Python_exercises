# Escribí un programa que solicite al usuario que ingrese cuántos shows musicales ha visto en el último año y almacene ese número en una variable. A continuación mostrar en pantalla un valor de verdad (True o False) que indique si el usuario ha visto más de 3 shows.

# Ejemplo de ejecución:

# Shows vistos en el último año: 3
# False

# Código de ejemplo

# print(58273%10)
# print(58273//10)

#La primera instrucción imprimirá el número 3, ya que es el resto de la división de 58273 por 10. La segunda instrucción imprimirá 5827, ya que es la parte entera del resultado de dividir 58273 por 10. Estas operaciones matemáticas son estrategias que se pueden utilizar para obtener partes de un número.

vistas = int(input("vistas a resitales: "))

if vistas > 3:
    print(True)
else:
    print(False)