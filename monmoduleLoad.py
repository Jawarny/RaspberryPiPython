import json
import os
import codecs

#Jawarny
with open(os.path.join(os.path.dirname(__file__), "test.json"), encoding='utf-8') as fichierJson:
    lesDonneJawarny = json.load(fichierJson)
    print(lesDonneJawarny)

#khoye     
with codecs.open("test.json", encoding="utf-8") as fichierJson:
    lesDonneKhoye = json.load(fichierJson)
    print(lesDonneKhoye)
#kamikase       
with open("test.json", encoding='utf-8') as fichierJson:
    lesDonneKamikase = json.load(fichierJson)
    print(lesDonneKamikase)