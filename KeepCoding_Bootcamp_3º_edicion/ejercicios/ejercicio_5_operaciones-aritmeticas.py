numero1 = input("Primer valor :")
numero2 = input("Segundo valor :")

def validar(val1, val2):
    if val1.isdigit() == True and val2.isdigit() == True:
        val1 = int(val1)
        val2 = int(val2) 
        
    elif val1.isdigit() == False:
        val1 = input("Error,inserte un valor :")
    elif val2.isdigit() == False:
        val2 = input("Error,inserte un valor :")

    return int(val1), int(val2)



if validar(numero1, numero2):
    numero1 = int(numero1)
    numero2 = int(numero2)
    suma = numero1 + numero2
    resta = numero1 - numero2
    producto = numero1 * numero2
    division = numero1 / numero2

    
    print(":::::::::")
    print("Suma :{} Resta :{} Producto :{} División :{} ".format(round(suma,2),round(resta,2),round(producto,2),round(division,2)))


