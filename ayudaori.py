import math
w = 104.72 #rad/s
AB = 0.06 #m
BD = 0.16 #m
VB = 6.2832 #m/s
alfa = math.radians(60) #grados
alfa2 = math.radians(78.95)
beta2 = math.radians(71.05)
gama2 = math.radians(30)
sumangulostotales = 180
alfadegree = 60

#calculo angulos
gama = ((AB * math.sin(alfa))/ BD)
ig = math.radians(gama)
invergama = math.asin(gama)
convinver = math.degrees(invergama)
beta= (sumangulostotales-alfadegree-convinver)
abeta = math.sin(beta)

#velocidad VD
VD = (VB*math.sin(alfa2))/math.sin(beta2)

#velocidad angular Wbd
VD_B = (VB*math.sin(gama2))/math.sin(beta2)
Wbd = VD_B/BD

#datos
#print(sumangulostotales)
print(abeta)
print(gama)
print(invergama)
print(convinver)

print("beta=",beta)
print("VD_B=",VD_B)
print("VD=",VD)
print("Wbd=",Wbd)

print('Este es un hola para probar el resultado')