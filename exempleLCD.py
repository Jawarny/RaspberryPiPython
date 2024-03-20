import LCD1602
import time
import random

def initialisation():
    LCD1602.init(0x27, 1)
    
    LCD1602.write(0,0,"R")
    LCD1602.write(1,0,"a")
    LCD1602.write(2,0,"a")
    LCD1602.write(1,1,"Mubarak!")
    


lignes = [0,1]
ligne = random.choice(lignes)
debut = 0
#message = "Ramadan Mubarak"
message = "Ramadan"
tableauMessage = []

def initialisationJawarny():
    LCD1602.init(0x27, 1)
    changerMessageEnTableau(message)
    afficherMessage(debut, tableauMessage, ligne )
    
def fin():
    GPIO.cleanup()
    
def changerMessageEnTableau(message):
    for letter in message:
        tableauMessage.append(letter)

def afficherLettre(debut, lettre, ligne):
        LCD1602.write(debut,ligne, lettre)
        if debut == 15:
            debut = 0
        else: 
            debut += 1

def afficherLettres(debut, tableauMessage, ligne):
    
    for lettre in tableauMessage:
        afficherLettre(debut, lettre, ligne)
        debut += 1

def afficherMessage(debut, tableauMessage, ligne ):
    indexEcran = 0
    while indexEcran < 16:
        
        afficherLettres(debut, tableauMessage, ligne)
        time.sleep(0.15)
        LCD1602.clear()
        debut += 1
        indexEcran += 1
        # 012345    0 len(value) = 6 donc len(value) - 1 = index de la derniere lettre
    
#0 , 15
    
if __name__ == "__main__":
    try:
        #initialisation()
        initialisationJawarny()
    except KeyboardInterrupt:
        fin()