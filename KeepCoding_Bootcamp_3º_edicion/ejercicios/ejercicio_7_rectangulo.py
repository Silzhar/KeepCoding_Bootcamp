ancho = input("Ancho de la habitación  :")
fondo = input("Fondo de la habitanción  :")

formato = input("Elija formato: yardas (Y) o metros (M) : ")

def entradas(pared1 , pared2): #probar salida en tupla
    try:
        pared1 = int(pared1)

    except:
        while pared1 is not True:
            pared1 = input("Es necesario un valor numérico. Introduzca un número para el ancho :")
            if pared1.isdigit():
                pared1 = int(pared1)
                break

    try:
        pared2 = int(pared2)

    except:
        while pared2 is not True:
            pared2 = input("Es necesario un valor numérico. Introduzca un número para el fondo :")
            if pared2.isdigit():
                pared2 = int(pared2)
                break


    return pared1, pared2

if formato.upper() == 'M':
    metrosCuadrados =  entradas(ancho, fondo)

    if metrosCuadrados:
        ancho = metrosCuadrados[0]
        fondo = metrosCuadrados[1]

        superficie = ancho + fondo
        yardas = superficie / 0.9144
        print('')
        print("La habitación mide {} metros cuadrados, en yardas : {}".format(round(superficie, 2), round(yardas, 2)))


else:
    yardasCuadradas =  entradas(ancho, fondo)

    if yardasCuadradas:
        ancho = yardasCuadradas[0]
        fondo = yardasCuadradas[1]

        superficie = ancho + fondo
        metros = superficie * 0.9144
        print('')
        print("La habitación mide {} yardas cuadradas, en metros cuadrados : {}".format(round(superficie, 2), round(metros, 2)))