import json
#données d'un dictionnaire
personne_dict = {"nom" : "John Éric",
                 "language" : ["Java", "PHP"],
                 "age" : 33}

#ecriture deu dictionnaire dans un fichier json
#création du fichier si non existant
with open("personne.json", "w", encoding= "utf-8") as fic_json:
    json.dump(personne_dict, 
              fic_json, 
              ensure_ascii=False,
              indent=4,
              sort_keys=True)