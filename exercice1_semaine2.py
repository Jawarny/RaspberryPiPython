#lecture d'un mot
mot = input("Entrez le mot: ")
motValide = mot.upper()

listeMots = []

while motValide != "FIN":
    #ajout dans la liste
    listeMots.append(mot)
    
    #relecture d'un mot
    mot = input("Entrez le mot: ")
    motValide = mot.upper()

#afficher la liste avec le tri
listeMots.sort()
print(listeMots)