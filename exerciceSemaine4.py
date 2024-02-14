import tkinter as tk
from tkinter import *
from tkinter import messagebox
import re as regex

class fenetre:
    def __init__(self, principal):       
        self.principal = principal
        principal.title("Exercice - semaine 4")
        principal.geometry("450x125")
        
        
        self.frame_entrires = Frame(principal)
        self.frame_entrires.pack()
        
        #entry (saisie)
        label_nom_utilisateur = Label(self.frame_entrires, text="Nom d'utilisateur")
        label_nom_utilisateur.grid(column=0, row=0)
        
        self.entry_nom_utilisateur = Entry(self.frame_entrires,width=30)
        self.entry_nom_utilisateur.insert(0,"")
        self.entry_nom_utilisateur.grid(padx=5, pady=5,column=1, row=0)
        
        label_mot_de_passe = Label(self.frame_entrires, text="Mot de passe")
        label_mot_de_passe.grid(column=0, row=1)
        
        self.entry_mot_de_passe = Entry(self.frame_entrires,width=30, show="*")
        self.entry_mot_de_passe.insert(0,"")
        self.entry_mot_de_passe.grid(padx=5, pady=5,column=1, row=1)
        
        self.frame_bouton_valider = Frame(principal)
        self.frame_bouton_valider.pack(side=RIGHT, padx=10)
        
        self.bouton_valider = Button(self.frame_bouton_valider,
                                      text="Valider le mot de passe")
        self.bouton_valider["command"] = self.bouton_valider_clicked
        self.bouton_valider.pack()
        
    def bouton_valider_clicked(self):
        #for char in self.entry_mot_de_passe:
            #if char.isdigit():
                #return True
                #return False
            
        if regex.match(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{10,}$', self.entry_mot_de_passe.get()):
            messagebox.showinfo("Validation du mot de passe","le mot de passe de " + self.entry_nom_utilisateur.get() + " est valide.")
        else:
            messagebox.showerror("Validation du mot de passe","le mot de passe n'est pas valide.")
        
if __name__ == "__main__":
    interface = tk.Tk()
    app = fenetre(interface) 
    interface.mainloop() 
