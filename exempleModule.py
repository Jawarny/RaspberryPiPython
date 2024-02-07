#accéder a module monmodule
import monmodule as mm
#méthode imprimer
def imprimer(txt):
    return print("Allo " + txt)

#utilisation du module
mm.imprimer("Simon")
pays = mm.professeur["pays"]
print(pays)

#importer seulement un élément
from monmodule import professeur as prof
print(prof)