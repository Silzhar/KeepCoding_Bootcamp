personas = input("Personas en reunión :")
porciones = input("Porciones por persona :")

def datos(participantes, comida):
    participantes = personas
    comida = porciones

    try:
        participantes = int(participantes)

    except:
        while participantes.isdigit() == False:
            participantes = input("Agregue  un numero y positivo de personas :")
            if participantes.isdigit():
                participantes = int(participantes)
                break


    try:
        comida = int(comida)

    except:
        while comida.isdigit() == False:
            comida = input("Agregue  un numero y positivo de pizzas :")
            if comida.isdigit():
                comida = int(comida)
                break

    return participantes, comida


validarDatos = datos(personas, porciones)


if validarDatos[0] % 2 == 0:  
    pizzas = validarDatos[0] / validarDatos[1]
    print("Total de pizzas  :{} ".format(pizzas))

elif validarDatos[0] % 2 != 0:
    pizzas = (validarDatos[0]+ 1) / validarDatos[1]
    print("Total de pizzas :{}, sobran {} trozos".format(round(pizzas), validarDatos[1]))

