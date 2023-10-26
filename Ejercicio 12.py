# Escribí un programa para solicitar al usuario el ingreso de un número entero y que luego imprima un valor de verdad dependiendo de si el número es par o no. Recordar que un número es par si el resto, al dividirlo por 2, es 0.
 
# Ejemplo de ejecución:

# Número entero: 7254
# True

# Código de ejemplo

# a=int(input())
# print(a>100  and  a!=1000)

#Primero se calcularán los valores lógicos (True o False) de las dos comparaciones: a > 100 y a != 1000 (lo cual dependerá del número guardado en la variable a). A continuación, se utilizará la tabla de verdad de la operación AND para calcular el resultado.

entero = int(input("ingrese un numero: "))

if entero % 2 == 0:
    print(True)
else:
    print(False)