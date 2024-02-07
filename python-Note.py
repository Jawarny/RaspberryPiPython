#  How to comment :
#  comemnt on that

""" 
AYO long comment here
Wassup with you!
"""

#  How to show simple information :
#  1)-----
nom = "Elias"
print("Votre nom est : ", nom)
#  2)-----
print("Votre nom est : " + nom)


#  How to initialize values :

nom = "Elias"	
nombre = 1 		# nombre est de type int
nombre = "un" 	# nombre est de type string
nom = str(1) 	# nombre est de type string '1' (Char)
nom = str(10)	# nombre est de type string "10" (Char)
nombre = int(1) # nombre est de type int 1
reel = float(1) # nombre est de type float 1.0


#  How to know the type of a value : 
nom = "Elias"
age = 26
print(type(nom))		# affichera <class 'str'>
print(type(age))		# affichera <class 'int'>

#  Different possible types les plus utiliser dans python : 
"""
str
int
float
bool
list, truple, range, dict, set # Structure de donnée
"""


#  --Strings!

var = "bonjour"
print(var)						#Affichera bonjour
print(var[0])					#Affichera b
print(var.replace('b','p'))		#Affichera ponjour
print(var.capitalize())			#Affichera Bonjour
print(var.upperr())				#Affichera BONJOUR
print(','.join(var))			#Affichera b,o,n,j,o,u,r  //prend la valeur dans le '' et separe le tout avec.
print(var[1:3])					#Affichera on //commence a la valeur 1 (inclusivement) affiche jusqua 3 (exclusivement)
print(var[0:-1])				#Affichera bonjou //commence a la valeur 0 (inclusivement) affiche tout supprimant -(1) caractere
print(var[1:-3])				#Affichera onj //commence a la valeur 1 (inclusivement) affiche tout supprimant -(3) caractere
print(var[:-1])					#Affichera bonjou //commence a la valeur 0 (inclusivement) affiche tout supprimant -(1) caractere
print(var[1:len(var)])			#Affichera onjour //commence a la valeur 1 (inclusivement) affiche tout jusqua la valeur len(var) (la longeur du string (Exclusivement))
print(var[1:])					#Affichera onjour //commence a la valeur 1 (inclusivement) affiche tout jusqua la valeur (longueur de la string(Exclusivement))
print("p" + var[1:])			#Affichera ponjour // affiche p ajoute a coter var commence a la valeur 1 (inclusivement)

print(len(var))					#Affichera 7 //la longueur de la string en int

var = "bonjour tout le monde"
print(var.split())				#Affichera ['bonjour', 'tout', 'le', 'monde']
var = " bonjour tout le monde "
print(var.split())				#Affichera ['','bonjour', 'tout', 'le', 'monde','']
print(var.strip())				#Affichera "bonjour tout le monde"




#  Exercice -

nom = input("entrer votre nom : ")
print(nom)
text = "Hey, j'ai 15 ans."
print(text[0:3])
print(text[0:-5], "pommes.")
print(len(text))
print(text[0:len(text)].upper())
age = 26
salaire = 23.50

print("Bonjour mon nom est",nom,"j'ai ",float(age),"ans et mon salaire de l'heure est de", int(salaire), ".")

note = input("entrez votre note : ")
note = int(note)

if note >= 0 and note <= 101:
    pass
    if (note >= 60 and note < 101):
        print("Tu passe ton cours de fraçais")
    elif (note < 60):
       print("Tu coule ton cours de fraçais") 
    else:
        pass
else:
    print("la note dois être entre 0 et 100")
    
noteEnLettre = input("entrez votre note : ")
noteEnLettre = int(noteEnLettre)

if note >= 0 and note <= 101:
    if (note < 60):
        print("E")
    elif (note < 70):
       print("D") 
    elif (note < 80):
       print("C") 
    elif (note < 90):
       print("B")
    else:
        print("A")
        
note = [89,78,0,60,64]

#if not i == 0
#    for i in note:
#       print("élement à \" l'index" + str(note.index(i)) + " : " + str(i) + "%")
