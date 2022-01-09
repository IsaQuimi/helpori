import math

import numpy
import numpy as np
w = 104.72  # rad/s
AB = 0.06  # m
BD = 0.16  # m
VB = 6.2832  # m/s

datos = [[], [], []]
angulo = []
theta = []
beta = []
omega = []
datosB = [[], [], []]
cmtheta = []
cmbeta = []
complemento = []
VDB = []
vel = []
wbd = [[], [], []]


# crear los angulos
for i in range(0, 190, 10):
    angulo.append(i)
#angulo0 = np.arange(0, 190, 10)
#angulo0 = angulo0(3, 6)
#print(angulo0)

for i in range(0, 190, 10):
    res = (numpy.pi * i) / 180
    theta.append(res)
    rounded_arraytheta = np.round([theta],
    decimals=4)
    #print(rounded_arraytheta)
    #print(theta)


def calcular_angulos(theta):
    Bta = ((AB * np.sin(theta)) / BD)
    inverBta = math.asin(Bta)
    return inverBta
    # coninver = math.degrees(inverBta)
    # return coninver


for i in theta:
    angulo_calculado = calcular_angulos(i)
    beta.append(angulo_calculado)
    rounded_arraybeta = np.round([beta],
                                  decimals=4)
    #print(rounded_arraybeta)
    # print(beta)


def calcular_omega(theta, beta):
    #while i < 180:
     omega = (numpy.pi - theta - beta)
     return omega

#Obtenemos la misma cantidad de elemento en cada array
#Por lo tanto tenemos la misma cantidad de iteraciones
#Al recorrerlo


#PROCEDEMOS DE USAR LA FUNCION calcular_omega con los valores theta y betha

#recorremos el array por medio de un ciclo for

for i in range(0, len(theta)):
    omega_calculado = calcular_omega(theta[i], beta[i])
    #como se puede observar, lo que se hizo fue que la i
    #sea el numero que cambia por el bucle, pero que corresponde
    #al mismo elemento de cada array
    #ejemplo:
    #for 1 in theta:
    #   omega_calculado = calcular_omega(theta[1], beta[1])
    #asi calculamos exactament 19 omegas co cada theta y cada beta
    omega.append(omega_calculado)


print(theta)
print(beta)
print(omega)

print(len(theta))
print(len(beta))
print(len(omega))


# ESTOY COMENTANDO PORQUE QUIERO HACER UN BUCLE NUEVO


#for i in theta:
    #for j in beta:
# while i < 180 and i < 180:
#         ang1 = (i)
#         ang2 = (i)
#         angomega = calcular_omega (theta, beta)

#         omega.append(angomega)
        #rounded_arrayomega = np.round([omega],
                                     # decimals=4)
        #print(rounded_arrayomega)
        # print(omega)


# crear 2ndos angulos
def calcular_comtheta(theta):
    cmth = ((math.pi / 2) - theta)
    return cmth


# for i in theta:
#     compt_cal = calcular_comtheta(i)
#     cmtheta.append(compt_cal)
    #print(cmtheta)


# def calcular_combeta(beta):
#     cmbt = ((math.pi / 2) - beta)
#     return cmbt


# for i in beta:
#     compb_cal = calcular_combeta(i)
#     cmbeta.append(compb_cal)
    #print(cmbeta)


# def calcular_omegacom(cmtheta, cmbeta):
#     _oomega = (math.pi - cmtheta - cmbeta)
#     return _oomega


# for i in cmtheta:
#     for j in cmbeta:
#         OMEGAcomplemento = calcular_omegacom(i, j)
#         complemento.append(OMEGAcomplemento)
#         #print(complemento)


#def VD_B(cmtheta):
    #velocidad1 = (VB * math.sin(cmtheta))
    #return velocidad1
#def VD_B2(VD_B, cmbeta):
    #velocidadB = VD_B/math.sin(cmbeta)
    #return velocidadB

#for i in range(20):
    #for j in  range(20):
        #calVDB = VD_B2(VD_B, cmtheta)
        #VDB.append(calVDB)
        #print(VDB)
    #velocidad1 = ((VB * math.sin(cmtheta)) / math.sin(cmbeta))
    # velocidad VD
    #VD = (VB * math.sin(alfa2)) / math.sin(beta2)

    # velocidad angular Wbd
   #
#     #Wbd = VD_B / BD

# print(angulo)
#import numpy as np
#rounded_arraytheta = np.round([theta],
                         #decimals=4)
#print(rounded_arraytheta)
#rounded_arraybeta = np.round([beta],
                         #decimals=4)
#print(rounded_arraybeta)
#rounded_arrayomega = np.round([omega],
                        # decimals=4)
#print(rounded_arrayomega)

#print(rounded_array)
# datos = ([theta,beta,omega])
# datosB = [cmtheta, cmbeta, complemento]
# print(datosB)
# print(datos)

