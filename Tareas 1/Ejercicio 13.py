# Escribí un programa que le solicite al usuario su edad y la guarde en una variable. Que luego solicite la cantidad de artículos comprados en una tienda y la guarde en otra variable. Finalmente, mostrar en pantalla un valor de verdad (True o False) que indique si el usuario es mayor de 18 años de edad y además compró más de 1 artículo.
 
# Ejemplo de ejecución:

# Tu edad: 32
# Artículos comprados: 1
# False

edad = int(input("ingrese su edad: "))

compra = int(input("cantidad de compras: "))

if edad > 18:
    if compra > 1:
        print(True)
    else:
        print(False)
else:
    print("Eres menor de edad")