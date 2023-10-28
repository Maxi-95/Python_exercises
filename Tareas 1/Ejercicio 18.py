# Escribí un programa que solicite al usuario el ingreso de dos números diferentes y muestre en pantalla al mayor de los dos.
 
# Ejemplo de ejecución:

# Un número: 592
# Otro número distinto: 1726
# 1726 es mayor

numero1 = int(input("ingrese un numero: "))
numero2 = int(input("ingrese otro un numero: "))

if numero1 > numero2:
    print(numero1)
elif numero1 < numero2:
    print(numero2)
else:
    print("los dos numero son iguales")