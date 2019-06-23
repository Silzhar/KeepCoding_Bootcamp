nombre = input("Ingrese un nombre :")
verbo = input("Ingrese verbo :")
advervio = input("Ingrese advervio :")
adjetivo = input("Ingrese adjetivo :")



if verbo == "matar" or "ejecutar" or "eliminar":
    historia2 = ("Miles de años llevan los gatos preparando la conquista del planeta.\n"
            "Han sido laboriosos los esfuerzos por encontrar las debilidades de otras espécies.\n"
            "{},el lider supremo ha convocado una reunión extraordinaria\n"
            "Después de la reunión del Clan de la Zarpa de este año salieron dos conclusiones :\n"
            "1:Se determina una acción contra la raza humana :{}\n"
            "Cuando se decida {}, la acción 1 se pasará a fase 2: la asignación del agente\n"
            "el designado  será Executus al ser el más {}. Comienza el extermínio".format(nombre,verbo,advervio,adjetivo))

    print("-------------------------------------------")
    print("\n")
    print(historia2)
    print("\n")
    print("-------------------------------------------")

else:
    historia = ("Miles de años llevan los gatos preparando la conquista del planeta.\n"
            "Han sido laboriosos los esfuerzos por encontrar las debilidades de otras espécies.\n"
            "{},el lider supremo ha convocado una reunión extraordinaria\n"
            "Después de la reunión del Clan de la Zarpa de este año salieron dos conclusiones :\n"
            "1:Se determina una acción contra la raza humana :{}\n"
            "Cuando se decida {}, la acción 1 se pasará a fase 2: la asignación de agentes\n"
            "2:Los designados para el comienzo de tal función son Executus y Apocalipsis\n"
            "El que tomará las decisiones será Executus al ser el más {}".format(nombre,verbo,advervio,adjetivo))

    print("-------------------------------------------")
    print("\n")
    print(historia)
    print("\n")
    print("-------------------------------------------")