#exemple interface avec classe
import tkinter as tk
#from tkinter import tkk

class fenetre(tk.Tk):
    #constructeur
    def __init__(self):
        super().__init__()
        
        #configuration de notre fenêtre 
        #titre, size and other
        self.title("Exemple fenêtre classe POO")
        self.geometry("1280x720")
        
        # ... création des widgets
    
    #ajouter des méthodes dans notre classe : méthodes sur les événements des widgets

#programme principale
if __name__ == "__main__":
    app = fenetre() #création de notre  objet fenêtre
    app.mainloop() #afficher la fenêtre 
