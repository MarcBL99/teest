import funcions

print("1-Endevina el número")
print("2-Pedra paper o tisores")
print("3-Ahorcado")
menu= int(input("Selecciona a quin joc vols jugar:"))

while menu < 0 or menu > 3:
    menu= int(input("Escull una opció vàlida:"))

if menu == 1:
    funcions.adivinaNumero()

    
if menu ==2:
    funcions.pedraPaperTisores()

if menu == 3:
    funcions.ahorcado()