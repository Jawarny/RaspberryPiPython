notes = [89, 76, 0, 54, 98]

# création d'un tableau
langage = ["c#", "python", "java", "sql"]
print(langage)

# ajout élément
langage.append("php")
print(langage)

#enleve élément à l'index demandé
langage.pop(2)
print(langage)

#ajout élément avec un index
langage.insert(3, "kotlin")
print(langage)

nombres = list([45, 76, 89, -1, 23])

#fusionner les listes : peut avoir plusieurs types d'éléments > string, int, float, etc
nombres.extend(langage)
print(nombres)

# parcourir notre liste : boucle for
print("#### parcourir avec boucle for")
for i in langage :
    print(i)

#parcourir avec index
print("#### parcourir avec index boucle for")
for i in range(len(langage)):
    print(langage[i])

# syntaxe courte
print("#### syntaxe courte boucle for parcourir")
[print(i) for i in langage]

# boucle while
print("parcourir avec boucle while")
ctr = 0
while ctr < len(langage):
    print(langage[ctr])
    ctr+=1 # ou ctr = ctr + 1
    
nombres2 = list([45, 76, 89, -1, 23])

# ordre croissant
print (" avant tri : ", nombres2)
nombres2.sort()
print (" après tri : ", nombres2)

# ordre décroissant
nombres2.sort(reverse=True)
print (" après tri décroissant : ", nombres2)


