#creatrion d'une interface graphique   

#importation de tous les objets possible 
from tkinter import *

#creation d'une fenêtre
fenetre = Tk()

#titre à la fenêtre 
fenetre.title("Exemple d'une fenêtre")

#modifier la taille 
fenetre.geometry("1280x720")

#Widget étiquette (label)
lable_nom = Label(fenetre, text="Nom de la personne")
lable_nom.grid(column=0, row=0)

label_age = Label(fenetre, text="Age",  font=("Arial Bold", 20))
label_age.grid(column=1,row=1)

#widget text box 

#affichage de la fenêtre - Important!!
fenetre.mainloop()