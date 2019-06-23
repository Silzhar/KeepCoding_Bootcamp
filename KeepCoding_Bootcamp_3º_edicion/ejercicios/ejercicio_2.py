'''
string = input("Escriba aquí :")
totalLetras = len(string)
if len(string) == " ":
    totalLetras - 1
print("Total de letras :",totalLetras)


'''
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


string = input("Escriba aquí :")
totalLetras = 0

for abecedario in string:
    if abecedario in string:  # if abecedario.has_key(string):
        totalLetras += 1
        if len(string) == ' ':
            totalLetras - 1
            
    elif totalLetras == 0:
        print("Ha introdducido una cadena vacía")

print("Total de letras :",totalLetras)

'''
'''

import collections

string = input("Escriba aquí :")

for string in abecedario:
    totalLetras += collections.Counter(string)
    print("Total de letras :",totalLetras)

'''
# posible solucion al ejercicio. de momento funciona

from collections import Counter

string = input("Escriba aquí :")

print(Counter(string))