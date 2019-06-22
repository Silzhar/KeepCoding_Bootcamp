'''
string = input("Escriba aquí :")
totalLetras = len(string)
print("Total de letras :",totalLetras)
'''


abecedario = {
            'A','a',
            'B','b',
            'C','c',
            'D','d',
            'E','e',
            'F','f',
            'G','g',
            'H','h',
            'I','i',
            'J','j',
            'K','k',
            'L','l',
            'M','m',  
            'N','n',
            'Ñ','ñ',
            'O','o',
            'P','p',
            'Q','q',
            'R','r',
            'S','s',
            'T','t',
            'U','u',
            'V','v',
            'W','w',
            'X','x',
            'Y','y',
            'Z','z'

        }

'''
string = input("Escriba aquí :")

for string in abecedario:
    if abecedario.has_key(string):
        totalLetras += string
        print("Total de letras :",totalLetras)
    elif string in abecedario == 0:
        print("Ha introdducido una cadena vacía")
'''


import collections

string = input("Escriba aquí :")

for string in abecedario:
    totalLetras += collections.Counter(string)
    print("Total de letras :",totalLetras)
