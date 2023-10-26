# Escribí un programa que solicite al usuario una letra y, si es una vocal, muestre el mensaje “Es vocal”. Verificar si el usuario ingresó un string de más de un carácter y, en ese caso, informarle que no se puede procesar el dato.
 
# Ejemplo de ejecución:

# Letra: o
# Es vocal

letra = input("ingrese una letra: ")

if letra == "a":
    print("la letra es vocal")
elif letra == "e":
    print("la letra es vocal")
elif letra == "i":
    print("la letra es vocal")
elif letra == "o":
    print("la letra es vocal")
elif letra == "u":
    print("la letra es vocal")
else:
    print("la letra NO es vocal")