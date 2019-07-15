from math import ceil 

bote = 5
metrosBote = 100

anchoTecho = input("Introduzca el alcho del techo a pintar :")
fondoTecho = input("Introduzca el fondo del techo a pintar :")


def entradas(ancho, fondo):

    if ancho.isdigit():
        ancho = int(ancho)

    else:     
        while ValueError :
            ancho = input("Introduzca un número y que sea positivo para el ancho :")
            if ancho.isdigit():
                ancho = int(ancho)
                break


    if fondo.isdigit():
        fondo = int(fondo)
    else:
        while ValueError :
            fondo= input("Introduzca un número y que sea positivo para el fondo :")
            if fondo.isdigit():
                fondo = int(fondo)
                break

    return ancho, fondo
    

datos = entradas(anchoTecho, fondoTecho)


metrosTecho = datos[0] + datos[1]        
botesCompra = metrosTecho / metrosBote
pintura = (metrosTecho / metrosBote) * bote

print("Litros de pintura necesários : {}".format(round(pintura, 1)))
print("botes a comprar : {}".format(ceil(botesCompra)))

