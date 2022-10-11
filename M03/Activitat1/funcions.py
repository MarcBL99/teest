import random
#Definim una funció per a cada joc
def adivinaNumero():

    print("En aquest joc hauràs d´endevinar el número entre 1 i 10, tens 3 intents ")
    vides = 3
    numeroGenerat = random.randint(1,10)
    jocAcabat= False
    numerosIntroduits= []
    numerosPosibles= ["1","2","3","4","5","6","7","8","9","10"]
    numeroInt = 0
   # print("Numero generat: " + str(numeroGenerat))

    while jocAcabat == False:
        numero= input("Introdueix un numero entre 1 i 10 ")
        #Si el valor introduit no es troba a la llista es tindra que ingresar un nou valor valid
        while numero not in numerosPosibles:
            numero= input("Has d´introduir un numero entre 1 i 10 ")
        
        
        #Comprobació de que l´usuari no introdueixi un número repetit
        while numero in numerosIntroduits:
            numero= input("El número " + str(numero) + " ja ha sigut introduit, proba amb un altre ")
        
        numerosIntroduits.append(numero)

        #Paso el numero a int per poder comparar si es menor o major al numero generat
        numeroInt=int(numero)
        if numeroInt > numeroGenerat:
            vides= vides -1
            print("El número " + str(numeroInt) + " es major al numero generat, et queden " + str(vides) + " vides")   

        if numeroInt < numeroGenerat:
            vides= vides - 1
            print("El número " + str(numeroInt) + " es menor al numero generat, et queden " + str(vides) + " vides") 

        if numeroInt == numeroGenerat:
            print("Has guanyat!, el numero era el " + str(numeroGenerat))
            jocAcabat= True

        if vides == 0:
            print("El numero correcte era " + str(numeroGenerat) + ", has perdut")
            jocAcabat= True

def pedraPaperTisores():

    print("Juga a pedra paper o tisores contra la màquina: pedra guanya a tisores, tisores guanya pedra, paper guanya a pedra")
    victoriesJug1= 0
    victoriesJug2= 0
    jocAcabat = False
    opcions= ["pedra","paper","tisores"]
    
    while jocAcabat == False:
        jugada1= input("Escull una opció: paper, pedra o tisores\n")

        while jugada1 not in opcions:
            jugada1= input("Has introduit una opció no vàlida, escriu pedra, paper o tisores\n")
        
        jugada2= random.choice(opcions)
        #print("Jugada maquina: " + jugada)

        
        partida(jugada1,jugada2,victoriesJug1,victoriesJug2)

        

        if victoriesJug1 == 3:
            print("Has guanyat!")
            jocAcabat = True

        if victoriesJug2 == 3:
            print("La màquina ha guanyat")
            jocAcabat = True
        print("--------------------------")   

#Funció on s´analitzara el resultat i es sumaran els punts
def partida(j1,j2,vict1,vict2):
    #Per cada jugada del jugador 1 analitzem totes les jugades posibles i sumem el marcador de victories al jugador corresponent
        if j1 == "pedra":

            if j2 == "tisores":
                print("Has jugat amb pedra i la maquina ha jugat amb tisores, tu guanyes")
                vict1+= 1

            elif j2 == "paper":
                print("Has jugat amb pedra i la màquina ha jugat amb paper, guanya la maquina")
                vict2+= 1
        
        elif j1 == "tisores":

            if j2 == "pedra":
                print("Has jugat amb tisores i la màquina ha jugat amb pedra, guanya la maquina")
                vict2+= 1

            elif j2 == "paper":
                print("Has jugat amb tisores i la màquina ha jugat amb paper, tu guanyes")
                vict1+= 1
        
        elif j1 == "paper":

            if j2 == "tisores":
                print("Has jugat amb paper i la màquina ha jugat amb tisores, guanya la maquina")
                vict2+= 1
            elif j2 == "pedra":
                print("Has jugat amb paper i la maquina ha jugat amb pedra, tu guanyes")
                vict1+= 1
        
        elif j1 == j2:
            print("Els 2 jugadors han triat la mateixa opció, es un empat")
        
        print("Marcador: " + str(vict1) + "-" + str(vict2))

          
def ahorcado():
    print("El joc de l´Ahorcado, introdueix lletres fins que encertis la paraula")
    paraules = []
    paraulaVuida = []
    paraulaString = ""
    jocAcabat=False
    lletresIntroduides = []
    # Obrim el fitxer de les paraules i llegim totes les linies(paraules) del fitxer
    with open("paraules.txt") as f:
        paraula = f.readline().strip()
        paraules.append(paraula)
        while paraula:
            paraula = f.readline().strip()
            paraules.append(paraula)
    #Es selecciona automaticament una de les 30 paraules
    paraulaSeleccionada = random.choice(paraules)
    #print("Paraula seleccionada: " + paraulaSeleccionada)

    intents = 2 * len(paraulaSeleccionada)
    #print(str(intents))

    #S´afegeix un "_" per cada lletra de la paraula
    for i in range (0,len(paraulaSeleccionada)):
        paraulaVuida += "_"
    
    
    while jocAcabat == False:  
        print("--------------------------")    
        #Fem un print de la paraula que estem adivinant, passantla a string per visualitzarla millor
        print("Paraula: " + str(paraulaString.join(paraulaVuida)))
        lletra= input("Introdueix una lletra : \n")
        
        
         
        #Si l´usuari introduiex mes d´una lletra, un numero o res se li tornara a preguntar
        while len(lletra) > 1 or lletra.isdigit() or lletra == "":
            lletra= input("Introdueix una sola lletra : \n")      
        

        while lletra.lower() in lletresIntroduides:
            lletra= input("La lletra " + lletra + " ja l´has introduit, proba amb un altre: \n")
        
        #Es pasa la lletra a miniscula, en cas que l´usuari l´ha escriguis en mayuscula
        lletra= lletra.lower()
        lletresIntroduides.append(lletra)

        if lletra in paraulaSeleccionada:
            print("La lletra " + lletra +  " es correcte")
            
        else:
            print("La lletra " + lletra + " no es correcte")
        
        intents-= 1
        print("Intents restants: " + str(intents))
        
        for n in range(0,len(paraulaSeleccionada)):
            #Es substitueix el "_" per la lletra introduida en la posició corresponent
            if lletra == paraulaSeleccionada[n]:
                paraulaVuida[n] = lletra
        
        if intents == 0:
            print("Has perdut, la paraula era " + paraulaString.join(paraulaSeleccionada))
            jocAcabat= True
        
        #Si no queden "_" vol dir que la paraula ja ha sigut encertada
        if "_" not in paraulaVuida:
            print("Has guanyat!")
            jocAcabat= True
        
        