
language = list("c#", "python", "java", "sql")
nombres = list([45,76,89,-1,23])
nombres2 = list([45,76,89,-1,23])

print ("parcourir avec boucle while")
[print(i) for i in language]

#boucle while 
print("parcourir avec boucle while")
ctrl = 0
while ctrl < len(language):
    print(language[ctrl])
    ctrl+=1 # ou ctrl = ctrl + 1

# ordre croissant
print ("avant tri : ", nombres2)
nombres2.sort()
print ("apres tri : ", nombres2)
#test
