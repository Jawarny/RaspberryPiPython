
import json;
import codecs;

nomFichier = "resultat.json"

try:
    with codecs.open(nomFichier, "r", encoding="utf-8") as fichierJson:
        lesParties = json.load(fichierJson)
except FileNotFoundError:
    lesParties = {"résultat": []}

i = 0
#dictionnaire
nouveauJoueur = {
    "nom": "Elias LOL",
    "age": 12,
    "pays": "quebec"
}  

while i < 4:
    lesParties["résultat"].append(nouveauJoueur) 
    i+=1  

# Write the data to the file (overwriting the existing content)
with codecs.open(nomFichier, "w", encoding="utf-8") as fichierJson:
    nouvellePartieJson = json.dumps(lesParties, ensure_ascii=False, indent=4)
    fichierJson.write(nouvellePartieJson)