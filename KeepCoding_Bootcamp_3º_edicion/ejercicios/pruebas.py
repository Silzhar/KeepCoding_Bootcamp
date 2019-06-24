

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

for x in string:
    if x in  abecedario:  
        totalLetras += 1
    if x == (' '):
        totalLetras - 1

print("Total de letras :",totalLetras)
