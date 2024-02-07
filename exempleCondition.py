# saisr une note
noteEntree = input("Entrez une note: ")
note = int(noteEntree)

# conditions
""" 
commentaires sur 
plusieurs lignes
"""
if (note >= 0 and note <= 100):
    print("note OK")
    if note < 60:
        print("Echec")
    else :
        print("Réussi")
    
    if note >=90 and note <= 100:
        print("Vous avez un A")
    elif note >=80 and note <= 89:    
        print("Vous avez un B")
    elif note >=70 and note <= 79:    
        print("Vous avez un C")
    elif note >=60 and note <= 69:    
        print("Vous avez un D")
    else:    
        print("Vous avez un E")
    
else:
    print("note entre 0 et 100")

#sortir de la condition : être a l'extérieur de l'indentation        