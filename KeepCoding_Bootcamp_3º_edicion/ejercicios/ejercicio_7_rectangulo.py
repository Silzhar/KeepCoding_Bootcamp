
ancho = input("Ancho de la habitación  :")
fondo = input("Fondo de la habitanción  :")

def entradas(dato1 , dato2):
    try:
        int(ancho)
        int(fondo)
        return True
    
    except:
        False
              

def habitacion(pared1, pared2):
    
    if pared1.isdigit():
        pared1 = int(pared1)
           
    else:
        while pared1 == False:
            pared1 = input("Es necesario un valor numérico. Introduzca un número para el ancho :")

    if pared2.isdigit():
        pared2 = int(pared2)
    
        
    else:   
        while pared2 == False:
            pared2 = input("Es necesario un valor numérico. Introduzca un número para el fondo :")
        

    return pared1, pared2
        


entradas(ancho, fondo)
metrosCuadrados = habitacion(ancho, fondo)

if metrosCuadrados:
    ancho = metrosCuadrados[0]
    fondo = metrosCuadrados[1]

    superficie = ancho + fondo
    yardas = superficie / 0.9144
    print("La habitación mide {} metros cuadrados, en yardas : {}".format(round(superficie, 2), round(yardas, 2)))