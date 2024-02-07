# afficher des données à l'écran
print("Bonjour à tous")

# saisir un nom
nom = input("Entrez votre nom: ")
print(nom)
print("type var nom :", type(nom))


# déclaration de variables
texte = "Objets connecté"
entier = 420
reel = 3.14
bool = True

# affiche le type
print("type entier ", type(entier))

# conversion
print("Entier converti en reel: ", float(entier))
print("Reel converti en entier: ", int(reel))

print("Résultat des deux nombres : ", float(entier) , " et ",  int(reel))
print("Résultat des deux nombres version 2: " + str(float(entier))  
      + " et " +  str(int(reel)))

#string
texte = "Objets connecté"
print(texte[0])
#texte[0] = "p"

print(texte[0:3]) # afficher 3 premières lettres
print(texte[0:-1]) # à partir de la fin
print(texte[0:len(texte)]) # méthode len = longueur string
print(texte.replace('b', 'p'))

# if...else : conditions




