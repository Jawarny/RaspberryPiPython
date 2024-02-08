class Etudiant:
    'classe de base pour la création d''un étudiant'
    
    # constructeur
    def __init__(self, pnom, pnoDA, pprogramme):
        # attribution des paramètres aux variables locales
        self.nom = pnom  
        self.noDA = pnoDA
        self.programme = pprogramme
        
    # permet d'afficher correctement notre objet à partir de liste : plus lisible
    def __repr__(self):
        return self.nom + "-" + self.noDA
        
    #méthode d'affichage
    def affichageEtudiant(self):
        print("Nom: " + self.nom + ", noDA: " + self.noDA)


# création d'un objet étudiant
etu1 = Etudiant("Simon Deschenes", "DESS123456", 420)
etu1.affichageEtudiant()
etu1.noDA = "DESS999999"
etu1.affichageEtudiant()
etu2 = Etudiant("John Doe", "DOEJ121212", 333)
listeEtudiants = [etu1, etu2]
print(listeEtudiants)
