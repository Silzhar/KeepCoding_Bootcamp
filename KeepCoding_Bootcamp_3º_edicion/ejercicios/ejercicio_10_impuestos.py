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



precios = []

def porcentaje(tasa):
    sumarTasa = []
    for precio in tasa:
        precioTasa = (precio * 5.5) / 100
        precios.append(precioTasa)

    for i in range(len(precios)):
        sumarTasa.append(precios[i]+tasa[i])
        

    return sumarTasa


totalObjetos = objetos() 
totalEntradas = entradas(Precios=[])
impuesto = porcentaje(totalEntradas)


print(".........................................................")
print(" ")
print("Precios sin impuesto :",totalEntradas)
print(" ")
print("Tasa aplicada de 5.5% sobre los valores anteriores :",precios)
print(" ")
print("Coste total :",impuesto)
print(" ")
print(".........................................................")