
import json;
import codecs;

nomFichier = "resultat2.json"

try:
    with codecs.open(nomFichier, "r", encoding="utf-8") as fichierJson:
        lesParties = json.load(fichierJson)
except FileNotFoundError:
    #lesParties = {"résultat": []}
    lesParties = {}


counter = len(lesParties) + 1
i = 0

# New entry to append
nouveauJoueur = {
    "nom": "Simon Deschennes",
    "age": 45,
    "pays": "Canada"
}

while i < 4:
      #lesParties["résultat"].append(nouveauJoueur)   
    lesParties[f"résultat{counter:02d}"] = [nouveauJoueur]
    counter += 1
    i+=1  

# Write the data to the file (overwriting the existing content)
with codecs.open(nomFichier, "w", encoding="utf-8") as fichierJson:
    nouvellePartieJson = json.dumps(lesParties, ensure_ascii=False, indent=4)
    fichierJson.write(nouvellePartieJson)