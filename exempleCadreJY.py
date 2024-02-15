import tkinter as tk
from tkinter import *

class fenetre(tk.Tk): #Tk erreur de frappe
    
    #constructeur
    def __init__(self, principal):
        self.principal = principal
        
        #self.principal = tk.Tk()
        
        #configuration de notre fenêtre 
        #titre, size and other
        principal.title("Exemple fenêtre classe POO")
        principal.geometry("1280x720")
        #principal_width, mprincipal_height = 1280, 720
        #self.principal.minsize(principal_width,mprincipal_height)
        
        #Création de cadre (frame)
        #cadre Défaut
        frame_default = Frame(principal)
        frame_default.pack()
        
        label_default = Label(frame_default, text="Default")
        label_default.pack()
        
        #cadre haut
        frame_haut = Frame(principal)
        frame_haut.pack(side=TOP)
        
        label_haut = Label(frame_haut, text="Haut")
        label_haut.pack()
        
        #cadre Bas
        frame_bas = Frame(principal)
        frame_bas.pack(side=BOTTOM)
        
        label_bas = Label(frame_bas, text="Bas")
        label_bas.pack()
        
        #cadre gauche
        frame_gauche = Frame(principal)
        frame_gauche.pack(side=LEFT)
        
        label_gauche = Label(frame_gauche, text="Gauche")
        label_gauche.pack()
        
        #cadre Droit
        frame_droit = Frame(principal)
        frame_droit.pack(side=RIGHT)
        
        label_droit = Label(frame_droit, text="Gauche")
        label_droit.pack()
        
         #cadre center
        frame_center = Frame(principal)
        frame_center.pack(fill=BOTH, expand=True)
        
        label_center = Label(frame_center, text="Center")
        label_center.pack(expand=True)
        
    #ajouter des méthodes dans notre classe : méthodes sur les événements des widgets

#programme principale
if __name__ == "__main__":
    interface = tk.Tk()
    app = fenetre(interface) #création de notre  objet fenêtre
    interface.mainloop() #afficher la fenêtre 
