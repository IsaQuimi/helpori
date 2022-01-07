
def run():
 
 Degrees = []
 for i in range (0, 190, 10):
        print(i)
        Degrees.append(i)
  
 print(Degrees)

import math
 
w = 104.72 #rad/s
AB = 0.06 #m
BD = 0.16 #m
VB = 6.2832 #m/s

alfa = math.radians(60) #grados #aqui es donde tiene que cambiar el grado
alfa2 = math.radians(78.95)
beta2 = math.radians(71.05)
gama2 = math.radians(30)
sumangulostotales = 180
alfadegree = 60 #aqui tambien <3


#calculo angulos
gama = ((AB * math.sin(alfa))/ BD)
ig = math.radians(gama)
invergama = math.asin(gama)
convinver = math.degrees(invergama)
beta= (sumangulostotales-alfadegree-convinver)
abeta = math.sin(beta)


if __name__ == '__main__' :
    run()