ficheroentrada = open('movimientos.txt', 'r')
ficherosalida = open('nuevosmovimientos.txt', 'w')

ix = input('Registro a borrar :')
ix = int(ix)

contador = 0


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