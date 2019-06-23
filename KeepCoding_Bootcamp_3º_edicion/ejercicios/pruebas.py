'''

string = input("Escriba aquí :")

totalLetras = 0

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

for letras in string:
    if string == abecedario:
        totalLetras += 1
    if letras == (' '):
        totalLetras - 1

print("Total de letras :",totalLetras)

'''

from collections import Counter

string = input("Escriba aquí :")

print(Counter(string))