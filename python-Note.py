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
nombre = 1 		    # nombre est de type int                    # ceci est équivalent a la ligne 25c
nombre = "un" 	    # nombre est de type string
nom = str(1) 	    # nombre est de type string '1' (Char)      # Aussi appeler Casting
nom = str(10)	    # nombre est de type string "10" (string)   # Aussi appeler Casting
nom = str(1.0)      # nombre est de type string "1.0" (string)  # Aussi appeler Casting
nombre = int(1)     # nombre est de type int 1                  # Aussi appeler Casting
nombre = int("1")   # nombre est de type int 1                  # Aussi appeler Casting

reel = float(1)     # nombre est de type float 1.0              # Aussi appeler Casting
reel = float("1")   # nombre est de type float 1.0              # Aussi appeler Casting
reel = float("1.0") # nombre est de type float 1.0              # Aussi appeler Casting


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

"""
+                   pour faire une addition, une combinaison de string ou peut aussi l’utiliser pour fusionner au moins deux listes
-                   pour faire une différence.
*                   Multiplication
/                   fait la division et retourne un nombre à décimal.
//                  fait la division, mais arrondi à l’entier inférieur
**                  Permet de calculer la puissance
%                   Permet de calculer le module
<, >, >=, <=        l’évaluation de la condition.
"""

"""
and, is             Retourne True si les deux valeurs sont vraies
or                  Retourne False si les deux valeurs sont fausse
not                 Retourne True si le résultat est faux
in                  Retourne True si une séquence avec une valeur spécifique est présente dans l’objet. 
=                   Permet d’affecter une valeur à une variable 
"""
print("hello" * 3)              #Affichera hellohellohello
#print("hello " * "world")      #Affichera une erreur peut pas multiplier une string avec une string seulement avec un int.

#  --Strings!

var = "bonjour"
print(var)						#Affichera bonjour
print(var[0])					#Affichera b
print(var.replace('b','p'))		#Affichera ponjour
print(var.capitalize())			#Affichera Bonjour
print(var.upper())				#Affichera BONJOUR
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
print(var.split(" "))			#Affichera ['','bonjour', 'tout', 'le', 'monde','']
print(var.strip())				#Affichera "bonjour tout le monde"

var = "Bonjour"
for char in var:
    print(char)                 #Affichera chaque lettre de bonjour sur une ligne avec la boucle.
if var < nom:                   #La comparaison de plus petit ou plus grand compare seulement le premier caractère de chaque string en unicode.
    place = " est avant "       #L'unicode qui est le plus petite sera placé avant dans cet exemple.
elif var > nom:                 #En d'autre mot aB < B = False  AB < B = True car A est l'unicode le plus petit suivi de B ensuite a (minuscule).
    place = " est après "
else:
    place =  " est à la même place que "
print("Le mot " + var + place + nom)

#print(2 + " + " + 2 + " = Quatre")  #Affichera un message d'erreur puisque pour afficher des strings avec des ints ou autre elle doit être converti avant
print(str(2) + " + " + str(2) + " = Quatre") #Affichera 2 + 2 = Quatre

print("%d + %d = %s" %(5,5,"dix"))                                                          #Affichera 5 + 5 = Dix
format = (5,5,"dix")    
print("%d + %d = %s" %format)                                                               #Affichera 5 + 5 = Dix
print("{chiffre00} + {chiffre01} = {mot00}".format(chiffre00=5,chiffre01=5, mot="dix"))     #Affichera 5 + 5 = Dix

valeur = True
valeur2 = False
print(valeur)               #Affichera True
print(valeur2)              #Affichera False
print(valeur is valeur2)    #Is est utiliser ici comme un ET comme un & comme un AND (True ET False = False) #Affichera False
print(valeur2 is valeur)    #Affichera False
print(valeur is valeur)     #Affichera True
if valeur: print("Vrai!")   #Afficera le print : Vrai!
if valeur2: print("Faux")   #Affiche rien car la condition est Fausse donc rentre meme pas dans le if

#if valeur:                 # ne pas oublier les (:)
    #code                   #contenu en tab pour etre dans le if
#elif valeur:               #elif c'est comme le else if dans java
    #code
    #break                  #peut utiliser un break malgré que ce n'est pas nécessaire
#else                       #le else à aussi besoin des deux points (:)

notes = [89,78,0,60,64]             # creation d'un tableau
for i in notes:
    if i == 60:
        break                       # quitte si c'est vrai!
    elif i >= 80:
        continue                    # utilisation de continue
    print("élement à l'index " + str(notes.index(i)) + " : " + str(i))  
    #Naffiche pas 89 puisquil est plus grand que 80 il retourne a la boucle sans continuer
    #Affichera ligne1: élement à l'index 1 : 78 
    #Affichera ligne2; élement à l'index 2 : 0
    #Naffiche pas 60 car le break le fait sortir de la boucle for
    
#boucle while
from time import sleep
temperature = 7

while temperature > 0:
    temperature = temperature - 1
    #temperature--                  #n'existe pas en python
    print("L'eay est à " + str(temperature) + " degrés\n" +
          "L'eau doit être plus froide pour former de la glace.")
    sleep(1)            #permet de faire une pause de 1 seconde
print("L'eau est à " + str(temperature) + ". Elle devrait se transformer en glace!")

#Affichera la temperature de leau de 6 a 1 avec le message et des intervales de 1 secondes ensuite affichera 0 directement.

age = 26
#texte = "mon nom est Elias et j'ai " + 26 + " ans."            #ERREUR puisqu'il va essayer d'additionner 26 au string il y a erreur.
texte = "mon nom est Elias et j'ai " + str(26) + " ans."        #on peut faire ça ou 
print(texte)                                                    #affichera mon nom est Elias et j'ai 26 ans.

texte = "mon nom est Elias et j'ai {} ans."                     
print(texte.format(age))                                        #affichera mon nom est Elias et j'ai 26 ans.

quantite = 4
noProduit = 123
prixProduit = 4.50
prixProduitFormate = "{:.2f}$".format(prixProduit)                                      # formatter un chiffre et garder 2 chiffre apres la virgule
totalFormate = "{:.2f}$".format(quantite*prixProduit)                                   # formatter un chiffre et garder 2 chiffre apres la virgule
commande = "Commande du produit {1} pour {0} items au prix de {2} à un total de {3}"    # voila comment afficher des valeurs avec format dans l'ordre voulu
print(commande.format(quantite, noProduit, prixProduitFormate, totalFormate))           # les valeurs peuvent etre placer comme voulu il faut juste sassurer quon les met a la bonne place


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
