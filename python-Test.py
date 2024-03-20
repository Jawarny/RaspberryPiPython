listeNoms = ["Lysa", "Elie Anne", "Elias", "Philippe"]
listeAutreNom = ["Khalid", "Latifa", "Naim"]

listeNoms = listeNoms + ["Micheline", "Adam", "Paolo"]              # Ajoute la liste a la liste initiale.
print(listeNoms)                                                    # Affichera ["Lysa", "Elie Anne", "Elias", "Philippe", "Micheline", "Adam", "Paolo"]
listeNoms.append("Suhas")                                           # Ajouteras "Suhas" à la fin de la liste.
print(listeNoms)                                                    # Affichera ['Lysa', 'Elie Anne', 'Elias', 'Philippe', 'Micheline', 'Adam', 'Paolo', 'Suhas']
listeNoms.insert(-3,"Basiliki")                                     # Ajoutera le nom "Basiliki" après  de l'index -3 commençant de la fin, c'est à dire sera a l'index -4
print(listeNoms)                                                    # Affichera ['Lysa', 'Elie Anne', 'Elias', 'Philippe', 'Micheline', 'Basiliki', 'Adam', 'Paolo', 'Suhas']
listeNoms.insert(3,"Sadaf")                                         # Ajoutera le nom "Sadaf" exactement a l'index 3
print(listeNoms)                                                    # Affichera ['Lysa', 'Elie Anne', 'Elias', 'Sadaf', 'Philippe', 'Micheline', 'Basiliki', 'Adam', 'Paolo', 'Suhas']
listeNoms.insert(3,"Suhas")                                         # J'ajoute  un nom a l'index 3 pour qu'il soit en double
print(listeNoms)                                                    # Affichera ['Lysa', 'Elie Anne', 'Elias', 'Suhas', 'Sadaf', 'Philippe', 'Micheline', 'Basiliki', 'Adam', 'Paolo', 'Suhas']
listeNoms.remove("Suhas")                                           # Supprimera la premiere occurence du nom "Suhas" et garde tout les autres
print(listeNoms)                                                    # Affichera ['Lysa', 'Elie Anne', 'Elias', 'Sadaf', 'Philippe', 'Micheline', 'Basiliki', 'Adam', 'Paolo', 'Suhas']
listeNoms.sort()                                                    # Arrangera la liste en ordre alphabetic de A à Z
print(listeNoms)                                                    # Affichera ['Adam', 'Basiliki', 'Elias', 'Elie Anne', 'Lysa', 'Micheline', 'Paolo', 'Philippe', 'Sadaf', 'Suhas']
listeNoms.sort(reverse=True)                                        # Arrangera la liste en ordre alphabetic de Z à A
print(listeNoms)                                                    # Affichera ['Adam', 'Basiliki', 'Elias', 'Elie Anne', 'Lysa', 'Micheline', 'Paolo', 'Philippe', 'Sadaf', 'Suhas']
                                   
listeNoms.append("alex")                                            
listeNoms.append("Alex")    
listeNoms.sort()                                                    # IMPORTANT A-Z en majuscule sera toujours mis avant les lettre minuscule Martin serais avant alex
print(listeNoms)                                                    # Affichera ['Adam', 'Alex', 'Basiliki', 'Elias', 'Elie Anne', 'Lysa', 'Micheline', 'Paolo', 'Philippe', 'Sadaf', 'Suhas', 'alex', 'alexandre']

nouvelleListeNoms = list(["Alex", "Jean-François", listeAutreNom ]) # Créer une liste avec les deux noms et a l'index 2 il y aura le tableau listeAutreNom
print(nouvelleListeNoms)                                            # Affichera ["Alex", "Jean-François",["Khalid", "Latifa", "Naim"]]

nouvelleListeNoms = list(["Alex", "Jean-François"])                 
nouvelleListeNoms.extend(listeAutreNom)                             # la bonne façon de le faire pour qu'il ajoute les valeurs c'est comme ça
print(nouvelleListeNoms)                                            # Affichera ['Alex', 'Jean-François', 'Khalid', 'Latifa', 'Naim']

nouvelleListeNoms = list(["Alex", "Jean-François", "Khalid", "Latifa", "Naim"])     
print("\n") 

for nom in nouvelleListeNoms:
    print(nom)
print("\n")    

[print(i) for i in nouvelleListeNoms]
print("\n")      

for index in range(len(nouvelleListeNoms)):
    print(nouvelleListeNoms[index])
print("\n") 

for index in range(len(nouvelleListeNoms)):                         # Affiche chaque nom de la liste 1 par un en utilisant l'index.
    print(str(index + 1) + " " + nouvelleListeNoms[index])
print("\n")       

for index, name in enumerate(nouvelleListeNoms):
    print(str(index + 1) + " " + name)
print("\n")   

index = 0
while index < len(nouvelleListeNoms):
    print(str(index + 1) + " " + nouvelleListeNoms[index])
    index = index + 1
print("\n")