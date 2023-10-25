# Escribí un programa que solicite al usuario el ingreso de dos palabras, las cuales se guardarán en dos variables distintas. A continuación, almacená en una variable la concatenación de la primera palabra, más un espacio, más la segunda palabra. Mostrá este resultado en pantalla.

# Ejemplo de ejecución:

# Primera palabra: derribando
# Segunda palabra: muros
# derribando muros

# Código de ejemplo

# frase="Estoy programando"
# print(frase[0])
# i=6
# print(frase[i])

# El operador [ ] (corchetes) permite obtener un carácter a partir de un string. La posición del carácter se indica entre los corchetes, ya sea ingresando directamente el número, con una variable que contenga un número o con una operación que de como resultado un número. Siempre, el primer carácter de un string estará ubicado en la posición 0.


primera_palabra = "derribando"

segunda_palabra = "muros"

print(primera_palabra + " " + segunda_palabra)