# accéder à mon module
import monmodule as mm

#utilisation du module
mm.imprimer("Simon")
pays = mm.professeur["pays"]
print(pays)

#importer seulement un élément
from monmodule import professeur
print(professeur)