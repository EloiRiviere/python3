import math
import random

nb = int (input())
rayon = float (input())

listeP =[]
for i in range(nb):
	point =(input())
	coord=point.split(' ',2)

	x=float(coord[0])
	y=float(coord[1])

	listeP.append((x,y))

listeP.sort()

#fonctions
def dist(p,q):
	distance=math.sqrt(((q[0]-p[0])**2)+((q[1]-p[1])**2))
	return distance


def isConflit(liste, rayon, pt):
	for i in liste:
		if(dist(pt,i) <= rayon):
			return True
	return False

#test 1
final = []

for i in listeP:
	if not isConflit(final,rayon,i):
		final.append(i)

print(len(final))
for n in final:
	print(str(n[0])+" "+str(n[1]))


#test 2

# listeT = sorted(listeP, reverse = True)

# final2 = []

# for i in listeT:
# 	if not isConflit(final2,rayon,i):
# 		final2.append(i)

# print(len(final2))
# for n in final2:
# 	print(str(n[0])+" "+str(n[1]))



#opti

#voisins={p:[q for q in v if dist(p,q)<=r and p!=q] for p in v}



#listeS = listeP.sort(key=lambda p:p[0]+p[1])
#print(listeS)