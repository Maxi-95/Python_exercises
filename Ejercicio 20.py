# Escribí un programa para solicitar al usuario tres números y mostrar en pantalla al menor de los tres.
 
# Ejemplo de ejecución:

# Primer número: 20
# Segundo número: 30
# Tercer número: 10
# Menor: 10

# Código de ejemplo

# n=int(input("Número:"))

# if n>10 and n<20:
#     print("Número correcto")
# else:
#     print("Número incorrecto")

# if n<10 or n>20:
#     print("Número incorrecto")
# else:
#     print("Número correcto")
    
#En las dos instrucciones if-else anteriores se toma como correcto a cualquier número entre 10 y 20, pero es necesario observar cómo los operadores < y > cambian y cómo el operador and cambia por or para lograr el mismo objetivo.

numero1 = int(input("Numero 1: "))
numero2 = int(input("Numero 2: "))
numero3 = int(input("Numero 3: "))

lista = [numero1, numero2, numero3]

if numero1 < numero2 and numero1 < numero3:
    print(numero1)
elif numero2 < numero1 and numero2 < numero3:
    print(numero2)
else:
    print(numero3)


