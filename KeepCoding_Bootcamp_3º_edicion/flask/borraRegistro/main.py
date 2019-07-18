ficheroentrada = open('movimientos.txt', 'r')
ficherosalida = open('nuevosmovimientos.txt', 'w')

ix = int(input('Registro a borrar :'))


contador = 1

for linea in ficheroentrada:
    if contador != ix:
        ficherosalida.write(linea)
    contador += 1
    
ficheroentrada.close()
ficherosalida.close()


'''
linea = ficheroentrada.readline()  

while linea != '': # no graba el archivo 

    while contador != ix:  
        try:
            linea = ficheroentrada.readline()
            ficherosalida.write(linea)
        except ValueError:
            print(ValueError)
        contador += 1

ficheroentrada.close()
ficherosalida.close()    

'''

'''

while contador != ix:  # borra el primer registro en lugar del registro elegido  ¿?
    ficheroentrada.readline()
    for linea in ficheroentrada :
        ficherosalida.write(linea)
       
    contador += 1  


while contador != ix:  # borra el segundo y el cuarto registro
    for linea in ficheroentrada :
        ficheroentrada.readline()
        ficherosalida.write(linea)
       
    contador += 1 
    
    

while contador != ix:  # sale en el registro que se ha de borrar
    try:
        linea = ficheroentrada.readline()
        ficherosalida.write(linea)
    except ValueError:
        print(ValueError)
    contador += 1


for linea in ficheroentrada:
    while contador != ix:
        ficheroentrada.readline()
        ficherosalida.write(linea)

        contador += 1

 '''