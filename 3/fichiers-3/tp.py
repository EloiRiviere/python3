import random
import math
from random import seed
from random import choice	

def dist(p,q):
	distance=math.sqrt(((q[0]-p[0])**2)+((q[1]-p[1])**2))
	return distance

def distF(finale):
	distance = 0
	for i in range(len(finale)):
		distance += dist(finale[i-1],finale[i])
	return distance

def testOPti(finale):
	a=0
	while a < len(finale)-1:
		c=0
		while c < len(finale)-1:
			# print("a",a,"c",c, "len", len(finale))
			if(a!=c and a!=c+1 and a+1!=c and dist(finale[a],finale[a+1])+dist(finale[c],finale[c+1]) > dist(finale[a],finale[c])+dist(finale[a+1],finale[c+1])):
				oldfinale = finale
				if(a < c):
					finale = finale[:a+1]+list(reversed(finale[a+1:c+1]))+finale[c+1:]
				else:	
					finale = finale[:c+1]+list(reversed(finale[c+1:a+1]))+finale[a+1:]
				a=-1
				break
			c=c+1
		a=a+1
	return finale

nb = int (input())
listeP =[]
for i in range(nb):
	point =(input())
	coord=point.split(' ',2)

	x=float(coord[0])
	y=float(coord[1])

	listeP.append((x,y))

listeP.sort()



#seed(6) - 11.25
#seed(10)
seed(10)
pointAlea=choice(listeP)

finale = []
distanceT = 0
finale.append(pointAlea)
listeP.remove(pointAlea)


while listeP:
	distanceMin = float("inf")
	p = finale[-1]
	for i in listeP:
		dTmp = dist(p,i)
		if(dTmp<distanceMin):
			distanceMin = dTmp
			pt = i
	finale.append(pt)
	distanceT += distanceMin
	listeP.remove(pt)


#if(nb < 10000):
yoopifinale=testOPti(finale)
#print(finale)
print(nb)
#print(distanceT)
print(distF(yoopifinale))
for n in yoopifinale:
	print(str(n[0])+" "+str(n[1]))
#else:
#	#print(finale)
#	print(nb)
#	#print(distanceT)
#	print(distF(finale))
#	for n in finale:
#		print(str(n[0])+" "+str(n[1]))