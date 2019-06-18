import morse

mensaje = input("Entrada de texto :")

telegrama = morse.toMorse(mensaje)
print(telegrama)

telegramaTraduccion = morse.toPlain(mensaje)
print(telegramaTraduccion)