

def validar(numeros):
    val1 = input("Primer valor :")
    
    if val1.isdigit() == True:
        val1 = int(val1)
        
    else:
        val1 = input("Error,inserte un valor :")
        if val1.isdigit():
            val1 = int(val1)
        
    val2 = input("Segundo valor :")
    
    if val2.isdigit() == True:
        val2 = int(val2)
       
    else:
        val2 = input("Error,inserte un valor :")
        val2 = int(val2)
        val2 = numero2
        return val2

    return val1 , val2


numero1 = val1
numero2 = val2

valores = validar(val1)

valor1 = valores[0]
valor2 = valores[1]



  #  valor1 = int(numero1)
  #  valor2 = int(numero2)
suma = valor1 + valor2
resta = valor1 - valor2
producto = valor1 * valor2
division = valor1 / valor2

    
print(":::::::::::::::::::::::::")
print("Suma :{} Resta :{} Producto :{} División :{} ".format(round(suma,2),round(resta,2),round(producto,2),round(division,2)))


'''
    if val1.isdigit() == int and val2.isdigit() == int:
        val1 = int(val1)
        val2 = int(val2)
        
    if val1.isdigit() == False:
        val1 = input("Error,inserte un valor :")
        val1 = int(val1)
    if val2.isdigit() == False:
        val2 = input("Error,inserte un valor :")
        val2 = int(val2)

    return val1, val2



    def validar(val1, val2):
    while val1.isdigit() == int and val2.isdigit() == int:
            try:
            val1 = int(val1)
            val2 = int(val2)
        except:
            val1 = input("Error,inserte un valor :")
            val2 = input("Error,inserte un valor :")

        return val1, val2

        '''

'''   
    elif val1.isalpha():
        val1 = input("Error,inserte un valor :")
        val1 = int(val1)
        val1 = numero1
        return val1
    
    elif val2.isalpha():
        val2 = input("Error,inserte un valor :")
        val2 = int(val2)
        val2 = numero2
        return val2   '''
