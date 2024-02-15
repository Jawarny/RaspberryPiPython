#print("hello" * "world")
#print("hello " * 3.5)

quantite = 4
noProduit = 123
prixProduit = 4.50
prixProduitFormate = "{:.2f}$".format(prixProduit)
totalFormate = "{:.2f}$".format(quantite*prixProduit)
commande = "Commande du produit {1} pour {0} items au prix de {2} à un total de {3}"
print(commande.format(quantite, noProduit, prixProduitFormate, totalFormate))