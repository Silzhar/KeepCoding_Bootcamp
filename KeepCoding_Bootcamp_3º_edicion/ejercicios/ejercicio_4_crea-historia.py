nombre = input("Ingrese un nombre :")
verbo = input("Ingrese verbo :")
advervio = input("Ingrese advervio :")
adjetivo = input("Ingrese adjetivo :")

historia = ("Miles de años llevan los gatos preparando la conquista del planeta.\n"
            "Han sido laboriosos los esfuerzos por encontrar las debilidades de otras espécies.\n"
            "{},el lider supremo ha convocado una reunión extraordinaria\n"
            "Después de la reunión del Clan de la Zarpa de este año salieron dos conclusiones :\n"
            "1:Se determina una acción contra la raza humana :{}\n"
            "Cuando se decida {},de la acción 1 se pasará a fase 2: la asignación de agentes\n"
            "2:Los designados para el comienzo de tal función son Executus y Apocalipsis\n"
            "El que tomará las decisiones será Executus al ser el más {}".format(nombre,verbo,advervio,adjetivo))


print(historia)