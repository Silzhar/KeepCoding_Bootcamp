import morse
import time
#from docx import Document

mensaje = input("Entrada de texto :")

telegrama = morse.toMorse(mensaje)
print(telegrama)

telegramaTraduccion = morse.toPlain(mensaje)
print(telegramaTraduccion)

print(time.strftime)