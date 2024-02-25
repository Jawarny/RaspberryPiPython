#importer la librairue
import json

client_json = '{ "nom" : "simon", "age" : 43}'

#Charger en dictionnaire
client_dict = json.loads(client_json)
print(client_dict)
print(client_dict["nom"])            

#convertir de dictrionnaure en json
etudiant = {"Nom" : "Simon", "programme" : 420}           
etudiant_json = json.dumps(etudiant, indent= 4)
print (etudiant_json)