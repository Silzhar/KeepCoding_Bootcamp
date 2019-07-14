from math import ceil 

bote = 5
metrosBote = 100

anchoTecho = int(input("Introduzca el alcho del techo a pintar :"))
fondoTecho = int(input("Introduzca el fondo del techo a pintar :"))

metrosTecho = anchoTecho + fondoTecho
botesCompra = metrosTecho / metrosBote

print("botes a comprar :{}".format(ceil(botesCompra)))