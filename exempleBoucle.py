# déclaration liste ou tableau
notes = [89, 78, 0, 60, 64]

#boucle for affiche l'index de la liste
for i in notes:
    if i == 60:
        break
    
    if i == 0:
        continue
    
    print("Élément à l'index " + str(notes.index(i)) + " : " + str(i))
