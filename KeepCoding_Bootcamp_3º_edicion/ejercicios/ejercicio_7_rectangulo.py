ancho = input("Ancho de la habitación  :")
fondo = input("Fondo de la habitanción  :")

def entradas(ancho, fondo):
    try:
        int(ancho)
        int(fondo)
        return True
    
    except:
        False
    

def habitacion(pared1, pared2):

    if entradas:
        pared1 = int(ancho)
        pared2 = int(fondo)
        superficie = pared1 + pared2
        yardas = superficie / 0.9144
        print("La habitación mide {} metros cuadrados, en yardas : {}".format(round(superficie, 2), round(yardas, 2)))

    return pared1, pared2
        
        

habitacion(ancho, fondo)