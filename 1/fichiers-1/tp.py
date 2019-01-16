from random import choice
from random import seed

def tri(liste):
    return sorted(liste,reverse=True)

nb = int (input())
tPack = int (input())
liste = [int (input()) for i in range(nb)]

listeS = tri(liste)

nbToursOpti = 15000

# print(nb)
# print(tPack)
# print(liste)
# print(listeS)

listeOpti = []

while listeS:
	listeOpti.append([])
	for x in listeS:
		if(sum(listeOpti[-1])+x <= tPack):
			listeOpti[-1].append(x)
			# # optimisation
			# if(sum(listeOpti[-1])+x == tPack):
			#  	break
	for x in listeOpti[-1]:
		listeS.remove(x)
# print(listeOpti)



# seed(16)
# alea = choice(listeOpti)
# listeOpti.remove(alea)


# Version for qui perd des trucs...

# for i in range(nbToursOpti):
# 	for elem in alea:
# 		added = False
# 		for boite in listeOpti:
# 			if(sum(boite)+elem <= tPack):
# 				boite.append(elem)
# 				added = True
# 				break;

# 		if not added:
# 				listeOpti.append([])
# 				listeOpti[-1].append(elem)

# 		alea.remove(elem)


#Version while qui marche pas sauf pour le 20 et le 1000

# for i in range(nbToursOpti):
# 	while alea:
# 		added = False
# 		for boite in listeOpti:
# 			if(sum(boite)+alea[0] <= tPack):
# 				boite.append(alea[0])
# 				added = True
# 				break;

# 		if not added:
# 				listeOpti.append([])
# 				listeOpti[-1].append(alea[0])

# 		alea.remove(alea[0])


print(len(listeOpti))

for listeS in listeOpti:
	for n in listeS:
		print(n)
	print()


# Début d'autre code

# listeOpti = [[ listeS[0] ]]
# del listeS[0]

# for i in range(len(listeS)) :
# 	j = 0
# 	while sum(listeOpti[i]) != 30 and j <= len(listeS):
# 		if sum(listeOpti[i]) + listeS[j] <= 30 :
# 			listeOpti[-1].append(listeS[j])
# 			listeS[j] = 0
# 			del listeS[j]
# 		j += 1
