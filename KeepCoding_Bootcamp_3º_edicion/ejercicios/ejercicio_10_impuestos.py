def objetos():
    totalObjetos = input("Ingrese el total de objetos a procesar :")
    
    try:
        totalObjetos = int(totalObjetos)
    except ValueError:
        while totalObjetos.isdigit() == False:
            print("-- Debe ingresar un valor positivo --")
            totalObjetos = input("Ingrese el total de objetos a procesar :")
            if totalObjetos.isdigit():
                totalObjetos = int(totalObjetos)
                break

    return totalObjetos

totalObjetos = objetos() 


def entradas(Precios=[]):
    
    contador = 0
    while contador < totalObjetos:
        entrada = input("Ingrese precio del producto :")

        try:
            entrada = int(entrada)
            Precios.append(entrada)
            contador += 1
        except ValueError:
            print("-- Debe ingresar un valor positivo --")
        
        
    return Precios

totalEntradas = entradas(Precios=[])


def porcentaje(tasa):
    precios = []
    sumarTasa = []
    for precio in tasa:
        precioTasa = (precio * 5.5) / 100
        precios.append(precioTasa)

    for i in range(len(precios)):
        sumarTasa.append(precios[i]+tasa[i])
        

    return sumarTasa

impuesto = porcentaje(totalEntradas)

print(totalEntradas)

print(impuesto)