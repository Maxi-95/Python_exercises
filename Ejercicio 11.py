# Escribí un programa que le solicite al usuario ingresar una fecha formada por 8 números, donde los primeros dos representan el día, los siguientes dos el mes y los últimos cuatro el año (DDMMAAAA). Este dato debe guardarse en una variable con tipo int (número entero). Finalmente, mostrar al usuario la fecha con el formato DD / MM / AAAA.
 
# Ejemplo de ejecución:

# Fecha en formato DDMMAAAA: 16112017
# 16 / 11 / 2017

fecha = input("Fecha en formato DDMMAAAA: ")

if len(fecha) == 8:
    dia = fecha[0] + fecha[1]

    mes = fecha[2] + fecha[3] 

    año = fecha[4] + fecha[5] + fecha[6] + fecha[7]

    fecha_correcta = f"{dia} / {mes} / {año}"
    print(fecha_correcta)
else: 
    print("la fecha que ingresaste debe tener 8(ocho) digitos")