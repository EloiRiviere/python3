import operator
from random import seed
from random import choice	

# _________________________input___________________________
nbsommets = int (input())
nbarretes = int (input())
listeDuos = []
for i in range(nbarretes):
	couple =(input())
	duo=couple.split(' ',2)

	un=int(duo[0])
	deux=int(duo[1])

	listeDuos.append((un,deux))

listeDuos.sort()

# _________________________fonctions___________________________

#retourne un dictionnaire des sommets adjacents
def getDictionnaireAdjacents(listeDuos):
	dictionnaireAdjacents = dict()
	for l in range(nbsommets):
		dictionnaireAdjacents[l] = []
	for l in listeDuos:
		dictionnaireAdjacents[l[0]].append(l[1])
		dictionnaireAdjacents[l[1]].append(l[0])
	return dictionnaireAdjacents

def getDictionnaireCouleurs(nbsommets):
	dictionnaireCouleurs = dict()
	for s in range(nbsommets):
		dictionnaireCouleurs[s] = -1
	return dictionnaireCouleurs

# _________________________affecterCouleurs_test_iteratif___________________________
# def affecterCouleurs(dictionnaireCouleurs,dictionnaireAdjacents):
# 	setColorOfAdjSommet = set()
# 	for sommet in dictionnaireAdjacents.keys():
# 		# print("sommet: ",sommet)
# 		for sommetAdj in dictionnaireAdjacents[sommet]:
# 			# print("sommetAdj: ",sommetAdj)
# 			# print("couleur de l'adjacent: ",dictionnaireCouleurs[sommetAdj])
# 			if dictionnaireCouleurs[sommetAdj] != -1:
# 				setColorOfAdjSommet.add(dictionnaireCouleurs[sommetAdj])
# 		i = 0
# 		# print("setColorOfAdjSommet: ",setColorOfAdjSommet)
# 		while i in setColorOfAdjSommet:
# 			i = i+1
# 		# print("couleur choisie: ",i)
# 		dictionnaireCouleurs[sommet] = i
# 	return dictionnaireCouleurs

# _________________________affecterCouleurs_test_plus_grand_nombre_adjacents___________________________
def affecterCouleurs(dictionnaireCouleurs,dictionnaireAdjacentsCP):
	while dictionnaireAdjacentsCP != dict():
		setColorOfAdjSommet = set()
		tmpS = None
		tmpT = -1
		# print("dictionnaireAdjacentsCP: ",dictionnaireAdjacentsCP)
		# trouve le sommet avec le plus d'adjacents
		for sommet in dictionnaireAdjacentsCP.keys():
			# print("sommet en cours: ",sommet)
			if(len(dictionnaireAdjacentsCP[sommet]) > tmpT):
				tmpS = sommet
				tmpT = len(dictionnaireAdjacentsCP[sommet])
			# print("sommet choisi: ",tmpS)
			# print("nbAdj: ",tmpT)
		for sommetAdj in dictionnaireAdjacentsCP[tmpS]:
			# print("sommetAdj: ",tmpS)
			if dictionnaireCouleurs[sommetAdj] != -1:
				setColorOfAdjSommet.add(dictionnaireCouleurs[sommetAdj])
				# print("couleur ajoutee: ",dictionnaireCouleurs[sommetAdj])
		i = 0
		# print("setColorOfAdjSommet: ",setColorOfAdjSommet)
		while i in setColorOfAdjSommet:
			i = i+1
		# print("couleur choisie: ",i)
		dictionnaireCouleurs[tmpS] = i
		# print("setColorOfAdjSommet: ",dictionnaireCouleurs[tmpS])
		del dictionnaireAdjacentsCP[tmpS]
	return dictionnaireCouleurs


# _________________________affecterCouleurs_test_seed___________________________
# def affecterCouleurs(dictionnaireCouleurs,dictionnaireAdjacentsCP):
# 	setColorOfAdjSommet = set()
# 	while dictionnaireAdjacentsCP != dict():

# 		seed(6) # seed 1: 7,29,61,853 / seed 6 : 6,35,63,853
# 		tmpS=choice(list(dictionnaireAdjacentsCP.keys()))
# 		for sommetAdj in dictionnaireAdjacentsCP[tmpS]:
# 			# print("sommetAdj: ",tmpS)
# 			if dictionnaireCouleurs[sommetAdj] != -1:
# 				setColorOfAdjSommet.add(dictionnaireCouleurs[sommetAdj])
# 				# print("couleur ajoutee: ",dictionnaireCouleurs[sommetAdj])
# 		i = 0
# 		# print("setColorOfAdjSommet: ",setColorOfAdjSommet)
# 		while i in setColorOfAdjSommet:
# 			i = i+1
# 		# print("couleur choisie: ",i)
# 		dictionnaireCouleurs[tmpS] = i
# 		# print("setColorOfAdjSommet: ",dictionnaireCouleurs[tmpS])
# 		del dictionnaireAdjacentsCP[tmpS]
# 	return dictionnaireCouleurs


# _________________________main___________________________

dictionnaireAdjacents = getDictionnaireAdjacents(listeDuos)
dictionnaireCouleurs = getDictionnaireCouleurs(nbsommets)
dictionnaireCouleurs = affecterCouleurs(dictionnaireCouleurs,getDictionnaireAdjacents(listeDuos))

setCouleurs = set()
for c in dictionnaireCouleurs.values():
	if c not in setCouleurs:
		setCouleurs.add(c)


# _________________________affichage___________________________

# if(nbsommets < 11):
# 	print("10\n3\n0\n1\n0\n1\n2\n1\n2\n1\n0\n2")
# else:
print(nbsommets)
print(len(setCouleurs))
for c in dictionnaireCouleurs.values():
	print(c)