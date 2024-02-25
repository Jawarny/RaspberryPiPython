
stop = False
def exercise1():
    try:
        print("Exercice - 02- python introduction page 5\n")
        #  Exercice - 02- python introduction page 5 
            # Vous devez créer un programme qui permet de saisir votre nom et de l’afficher à l’écran.
                #◦ Déclarez trois variables : une variable String, une variable Int et une variable Float.
                #◦ Affichez à l’écran le type des trois variables.
                #◦ Faites une conversion de la variable Int en Float et affichez le résultat.
                #◦ Faites une conversion de la variable Float en Int et affichez le résultat.
        
        nom = input("Entrer votre nom : ")
        if nom.upper() == "JY":
            nom = "Jawarny"
        print("Voila un affichage de votre nom " + nom)
        uneString = nom
        unInt = 26
        unReel = 23.97
        print("La première variable " + uneString + " est de type " + str(type(uneString)) + "\n" +     #Pour afficher une variable en utilisant type entouré de text (string)
            "La deuxième variable " + str(unInt) + " est de type " + str(type(unInt)) + "\n" +        #il faut l'enrober du formatting str() pour la convertir en string pour
            "La troisième variable " + str(unReel) + " est de type " + str(type(unReel)) + ".")       #pour laffichage même chose pour les valeurs int et float.
        print("\n\n\n")
        #Fin de l'exercice
    except Exception as e:
        return str(e)
        
def exercise2():
    try:
        print("Exercice - 02- python introduction page 12\n")
        #  Exercice - 02- python introduction page 12 
            #◦ Vous devez créer un programme qui permet de saisir le nom du cours, votre nom et le numéro du programme à l’écran.
                #◦ Affichez la longueur de la chaîne de caractères du nom du cours à l’écran
                #◦ Affichez une partie de la chaîne de caractères en utilisant les sous-chaînes
                #◦ Affichez les trois variables saisies à l’écran en utilisant les trois formatages possibles.

        
        cours = input("Entrer le nom de votre cours : ") # Programmation Python dans un environnement linux avec un raspberry Pi
        if cours.upper() == "JY":
            cours = "Programmation Python dans un environnement linux avec un raspberry Pi"
        nom = input("Entrer votre nom : ")
        if nom.upper() == "JY":
            nom = "Jawarny"
        programme = input("Entrer le numéro de votre programme : ")
        while not (programme.isdigit() or programme.upper() == "JY"):
            programme = input("⚠ ERREUR! Entrer le numéro de votre programme : ")
        if programme.upper() == "JY":
            programme = 420
        elif programme.isdigit():
            programme = int(programme)
            
        print("La longeur de la chaîne de caractères du nom de cours " + cours + " est de " + str(len(cours)) + " caractères.")
        print("Voila une partie de la chaîne de caractères : " + cours[0:20])
        #première façon d'utiliser le formattage
        print("\n\nPremière façon d'utiliser le formattage!")
        print("Votre cours est : %s\nVotre nom est : %s\nVotre numéro de programme est : %d" %(cours, nom, programme))
        #deuxième façon d'utiliser le formattage
        print("\n\nDeuxième façon d'utiliser le formattage!")
        format = (cours,nom,programme) 
        print("Votre cours est : %s\nVotre nom est : %s\nVotre numéro de programme est : %d" %format)                                                        
        #troisième façon d'utiliser le formattage   
        print("\n\nTroisième façon d'utiliser le formattage!")
        print("Votre cours est : {coursFormat}\nVotre nom est : {nomFormat}\nVotre numéro de programme est : {programmeFormat}".format(coursFormat=cours, nomFormat=nom, programmeFormat=programme))
        print("\n\n\n")
    except Exception as e:
        return str(e)
        #Fin de l'exercice

def exercise3():
    try:
        print("Exercice - 02- python introduction page 21\n")
        #◦ Vous devez créer un programme qui permet de saisir et valider des notes numériques d’un cours.
            #◦ Les notes doivent être entre 0 et 100 inclusivement et misent dans une liste.
            #◦ Pour sortir du programme, vous devez écrire -1 comme note.
            #◦ Ensuite, vous devez calculer la moyenne des notes
            #◦ On affiche la moyenne avec deux chiffres après la virgule en utilisant la fonction format
        motNumero = ["première", "deuxième", "troisième", "quatrième", "cinquième",
                    "sixième", "septième", "huitième", "neuvième", "dixième",
                    "onzième", "douzième", "treizième", "quatorzième", "quinzième",
                    "seizième", "dix-septième", "dix-huitième", "dix-neuvième", "vingtième"]
        #motNumero = ["première", "deuxième", "troisième", "quatrième", "cinquième"]
        sortie = 0
        notes = []
        
        print("Ceci est un programme pour vous aider a calculer votre moyenne générale!")
        sortie = input("Entrer votre " + motNumero[len(notes)] + " note :\t")     
        if sortie.upper() == "JY":
            notes = [89,80, 95, 96, 87, 87, 85, 88, 81, 97, 72, 99, 95, 100, 97, 88, 61, 81]
            sortie = '-1'
        while len(notes) < 2:                                                                  
            if not sortie.isdigit() or not (0 <= int(sortie) <= 100):                                                  
                print("⚠ ERREUR! Veuillez entrez une note valide entre 0 et 100!\n")
            else:
                notes.append(int(sortie))                                                                
            
            if len(notes) < 2:
                sortie = input("Entrer votre " + motNumero[len(notes)] + " note :\t")
        
        if sortie != '-1':    
            sortie = input("Entrer (-1) pour terminer ou \n" +
                        "Entrer votre " + motNumero[len(notes)] + " note :\t")
            
        while sortie != '-1':    
            if not sortie.isdigit() or not (-1 <= int(sortie) <= 100):                                   
                print("⚠ ERREUR! Veuillez entrez une note valide entre 0 et 100!\n")
            elif 0 <= int(sortie) <= 100:
                notes.append(int(sortie))                                                               
            
            if len(notes) < 20:
                sortie = input("Entrer (-1) pour terminer ou \n" +
                               "Entrer votre " + motNumero[len(notes)] + " note :\t")
            else:
                print("AVERTISSEMENT! Le logiciel peut juste traiter 20 notes à la fois!\n\n")
                sortie = '-1'
           
        print("De la {} note à la {} note vous avez une moyenne de {:.2f}%".format(motNumero[0], motNumero[len(notes)-1],calculerMoyenne(notes)))      
        print("\n\n\n")
    except Exception as e:
        return str(e)
        #Fin de l'exercice
        
#def exercise4():
#def exercise5():
#def exercise6():
#def exercise7():
#def exercise8():
#def exercise9():
#def exercise10():
#def exercise11():
#def exercise12():
#def exercise13():
#def exercise14():
#def exercise15():
#def exercise16():
#def exercise17():
#def exercise18():
#def exercise19():
#def exercise20():
#def exercise21():
#def exercise22():
#def exercise23():
#def exercise24():
#def exercise25():
#def exercise26():
#def exercise27():
#def exercise28():
#def exercise29():

def calculerMoyenne(tableMoyenne):
    total = 0
    for note in tableMoyenne:
        total = total + note
    moyenne = total/ len(tableMoyenne)
    return moyenne 



while not stop: 
    print("Menu:\n"+
          "\t1. Exercice - 02- python introduction page 5\n"+
          "\t2. Exercice - 02- python introduction page 12\n"+
          "\t3. Exercice - 02- python introduction page 21\n"+
          "\t69. Stop\n")
    choice = input("Entrer le numero de l'exercice que vous voulez executer ou tapez 'stop' pour arrêter le programme: ") #PROD
    #choice = '3' #DEV
    if choice == '1':  
        error_message = exercise1()
        if error_message:
            print("Error occurred 1. Exercice - 02- python introduction page 5:", error_message)
    elif choice == '2':  
        error_message = exercise2()
        if error_message:
            print("Error occurred in 2. Exercice - 02- python introduction page 12:", error_message)
    elif choice == '3':  
        error_message = exercise3()
        if error_message:
            print("Error occurred in 3. Exercice - 02- python introduction page 21:", error_message)
    elif choice.lower() == "stop" or choice == '69' or choice.lower() == "quit" or choice.lower() == "quitter" or choice.lower() == "arrete":
        stop = True
    else:
        print("\n\n⚠ Entrée invalide. Veuillez saisir un numéro correspondant à un exercice ou 'stop'.⚠\n" + 
              "⚠ Invalid input. Please enter a number corresponding to an exercise or 'stop'.⚠\n\n")

print("Le programme à été arrêter.")

        
        
