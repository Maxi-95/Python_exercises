print("Hola mundo")
b = 2
a = 2
c = a + b
print(c)

# datos_compuestos
lista = ["puerta", "ventana", "heladera"]
print(lista[2])

# tupla
tupla = ("perro","gato","elefante")
print(tupla[2])
# tupla[2] = "raton"
# print(tupla[2])

conjunto = {"puerta", "ventana", "heladera", 1, 2, 1.25, False }
#print(conjunto[2])


diccionario = {
    'nombre': "Maxi", 
    'apellido': "Perez",
    'edad': 28,
    'graduado': True
}
diccionario['nombre'] = "Lucas"
print(diccionario)

# operadores de comparacion
result1 = 5 == 6
print(result1)

# condicionales (if) (elif) (else)
contraseña_guardada = 123456
contraseña_ingresada = 123456

if contraseña_guardada == contraseña_ingresada:
    print("INGRESO CORRECTO")
else:
    print("INGRESO INCORRECTO")
    
# metodos
palabra = "futbol"
numeros = "6541826"
tiene_letra = palabra.index("t")
resultado = "natacion".upper()
es_numerico = numeros.isnumeric()
longitud = len(palabra)

print(resultado)
print(es_numerico)
print(longitud)

# funciones para aditar listas
la_lista = list(["pan", "salame", "queso", "huevo duro"])
la_lista2 = [5,6,4,3,2,8,7,9,1]
quitar_elemento = la_lista2.pop() 
ordenar = la_lista2.sort()
la_lista.reverse()
print(len(la_lista))
#print(la_lista2)
print(la_lista)

# diccionarios
objetoDirec = {
    'nombre' : "Guille",
    'apellido' : "Lescano",
    'edad' : 24
}
valor_eliminado2 = objetoDirec.pop("apellido")

mi_diccionario = {'a': 1, 'b': 2, 'c': 3}
valor_eliminado = mi_diccionario.pop('b')
print(valor_eliminado)
print(valor_eliminado2)
print("y ahora")

# IMPUTS (ideal para formularios)
nombre = input("ingresa un nombre: ")
print(nombre)
print("nombre")
print("atras")
  