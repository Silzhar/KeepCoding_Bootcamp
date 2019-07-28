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



print(totalEntradas)