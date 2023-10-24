# Escribí un programa que solicite al usuario dos números y los almacene en dos variables. En otra variable, almacená el resultado de la suma de esos dos números y luego mostrá ese resultado en pantalla.
# A continuación, el programa debe solicitar al usuario que ingrese un tercer número, el cual se debe almacenar en una nueva variable. Por último, mostrá en pantalla el resultado de la multiplicación de este nuevo número por el resultado de la suma anterior.

# Ejemplo de ejecución:

# Ingresá un número: 1
# Ingresá otro número: 2
# Suman: 3
# Ingresá un nuevo número: 3
# Multiplicación de la suma por el último número: 9

# pedir al usuario que ingrese el primer numero
numero1 = int(input("ingresa el primer numero: "))
# pedir al usuario que ingrese el segundo numero
numero2 = int(input("ingresa el segundo numero: "))

# pedir al usuario que ingrese el tercer numero
suma = numero1 + numero2

# pedir al usuario que ingrese el tercer numero
numero3 = int(input("ingresa el tercer numero: "))

# multiplicar el numero3 por suma
resultado = numero3 * suma

# resultado de la multiplicacion
print(resultado)