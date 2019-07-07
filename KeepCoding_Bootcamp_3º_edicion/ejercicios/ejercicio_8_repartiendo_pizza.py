personas = input("Personas en reunión :")
pizzas = input("Total de pizzas :")

def datos(participantes, comida):
    participantes = personas
    comida = pizzas

    try:
        participantes = int(participantes)

    except:
        while participantes.isdigit() == False:
            participantes = input("Agregue  un numero y positivo de personas :")
            if participantes.isdigit():
                participantes = int(participantes)


    try:
        comida = int(comida)

    except:
        while comida.isdigit() == False:
            comida = input("Agregue  un numero y positivo de pizzas :")
            if comida.isdigit():
                comida = int(comida)

    return participantes, comida


validarDatos = datos(personas, pizzas)


if validarDatos[0] % 2 == 0:  
    porciones = validarDatos[0] * validarDatos[1]
    print("Total de porciones  :{}".format(porciones))

elif validarDatos[0] % 2 != 0:
    porciones = (validarDatos[0]+ 1) * validarDatos[1]
    print("Total de porciones :{}".format(porciones))


 
