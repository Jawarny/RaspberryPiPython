class Etudiant :
    'classe de base pour la création d''un étudiant'
    
    #constructeur
    def __init__(self,pnom,pnoDA, pprogramme):
        # attribution des parametres aux variables locales
        self.nom = pnom
        self.noDA = pnoDA
        self.programme = pprogramme
    #permet d'afficher correctement notre objet a partir de listes
    def __repr__(self):    
        return self.nom + "-" + self.noDA + "-" + self.programme
    #Méthode d'affichage
    def affichageEtudiant(self):
        print("Nom: " + self.nom + ", noDA: " + self.noDA + ", programme: " + self.programme)
    
#Création d'un objet étudiant
etu1 = Etudiant("Simon Deschenes", "DESS123456", 420)
etu1.affichageEtudiant()
etu1.noDA = "EJ201489"
etu1.nom = "Elias Jawarny"
etu1.affichageEtudiant()

etu2 = Etudiant("John Doe", "DOEJ123456", 333)
listeEtudiants = [etu1,etu2]
print (listeEtudiants)