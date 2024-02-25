
import json;
import codecs;

nomFichier = "resultat3.json"

try:
    with codecs.open(nomFichier, "r", encoding="utf-8") as fichierJson:
        lesParties = json.load(fichierJson)
except FileNotFoundError:
    #lesParties = {"résultat": []}
    lesParties = []

i = 0

# New entry to append
nouveauJoueur = {
        "résultat": [
            {
                "nom": "Simon Deschennes",
                "age": 45,
                "pays": "Canada"
            }
        ]
    }

while i < 4:
      #lesParties["résultat"].append(nouveauJoueur)   
    lesParties.append(nouveauJoueur)
    i+=1  

# Write the data to the file (overwriting the existing content)
with codecs.open(nomFichier, "w", encoding="utf-8") as fichierJson:
    nouvellePartieJson = json.dumps(lesParties, ensure_ascii=False, indent=4)
    fichierJson.write(nouvellePartieJson)