#exemple avec Entry (saisie), Button (bouton) et Text (champ d'affichage)

#exemple interface avec classe
import tkinter as tk
from tkinter import *

class fenetre:
    #constructeur
    def __init__(self, principal):       
        self.principal = principal
        
        #configuration de notre fenetre
        principal.title("Exemple de Entry dans une fenetre")
        principal.geometry("350x200")
        
        # creation des cadres (frame)
        # cadre haut
        self.frm_haut = Frame(principal)
        self.frm_haut.pack(side=TOP)
        
        #entry (saisie)
        self.entry_nom = Entry(self.frm_haut,width=20)
        self.entry_nom.insert(0, "Nom de la personne")
        self.entry_nom.pack(padx=5, pady=5)
        
        #bouton
        self.frm_bouton = Frame(principal)
        self.frm_bouton.pack()
        
        self.bouton_afficher = Button(self.frm_bouton,
                                      text="Afficher le nom")
        self.bouton_afficher["command"] = self.btn_afficher_clicked
        self.bouton_afficher.pack()
        
        # cadre bas
        self.frm_bas = Frame(principal)
        self.frm_bas.pack(side=BOTTOM)
        
        #champ texte
        self.txt_afficher = Text(self.frm_bas)
        self.txt_afficher.pack()
        
        
    # ajouter des methodes dans notre classe : methode sur les evenements des widgets
    def btn_afficher_clicked(self):
        self.txt_afficher.insert(END,"Le nom de la personne est " + self.entry_nom.get())

#programme principal
if __name__ == "__main__":
    interface = tk.Tk()
    app = fenetre(interface) #creation de notre objet fenetre
    interface.mainloop() # afficher la fenetre
