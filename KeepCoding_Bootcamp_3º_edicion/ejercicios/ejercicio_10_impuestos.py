totalObjetos = int(input("Ingrese el total de objetos a procesar :"))



def entradas():
    
    contador = 0
    while contador <=totalObjetos:
        entrada = int(input("Ingrese precio del producto :"))
        contador += 1

    return entrada

totalEntradas = entradas()

