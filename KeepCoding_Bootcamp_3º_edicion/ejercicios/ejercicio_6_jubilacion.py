import time

edad = input("¿ Cual es su edad ? ")


if edad.isdigit():
    edad = int(edad)
else:
    edad = input("Debe introducir un número ")
    if edad.isdigit():
        edad = int(edad)


edadJubilacion = input("Edad de jubilación :")

if edadJubilacion.isdigit():
    edadJubilacion = int(edadJubilacion)
else:
    edadJubilacion = input("Debe introducir un número ")
    while edadJubilacion.isdigit() == False:
        if edadJubilacion.isdigit():
            edadJubilacion = int(edadJubilacion)


jubilacion = edadJubilacion - edad
añoActual = time.strftime("%Y")
añoActual = int(añoActual)
añoJubilacion = añoActual + jubilacion

print("Quedan {} años para su jubilación ".format(jubilacion))
print("Año actual : {} , año de jubilación : {}".format(añoActual, añoJubilacion))
