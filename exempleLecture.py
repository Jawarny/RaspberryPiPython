import json

#lecture à partir d'un fichier json
with open("data.json", encoding='utf-8') as fic:
    data = json.load(fic)
    
print(data)



data2 = ""
try:
    #lecture à partir d'un fichier json
    with open("data2.json", encoding='utf-8') as fic:
        data2 = json.load(fic)
        print("data : ", data2)
        data_liste = data["personne"]
        print("data_dicr : ", data_liste)
        #Si classe créer avec les éléments du json, commande ci-bas permette
        #data_liste.append(classecréer.__dict__)
        
except:
    print("Erreur de fichier") 
else:
    fic.close()  
finally:     
    print(data2)
    