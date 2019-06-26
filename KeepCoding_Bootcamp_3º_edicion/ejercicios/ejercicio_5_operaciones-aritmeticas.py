numero1 = input("Primer valor :")
numero2 = input("Segundo valor :")

def validar(val1, val2):
    if val1.isdigit() == True and val2.isdigit() == True:
        val1 = int
        val2 = int
        
    elif val1.isdigit() == False:
        val1 = input("Error,inserte un valor :")
    elif val2.isdigit() == False:
        val2 = input("Error,inserte un valor :")

validar(numero1, numero2)

suma = numero1 + numero2
resta = numero1 - numero2
producto = numero1 * numero2
division = numero1 / numero2

if validar == True :
    print("Suma :"+suma+"Resta :"+resta+"Producto :"+producto+"División :"+division)



'''
if numero1.isdigit() == True and numero2.isdigit() == True:
    numero1 = int
    numero2 = int
    print("Suma :",suma,"Resta :", resta,"Producto :",producto,"División :",division)

else:
    numero1 = input("Primer valor")
    numero2 = input("Segundo valor")
    '''