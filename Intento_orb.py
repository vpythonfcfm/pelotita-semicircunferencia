#Importaciones
from vpython import *
import numpy as np

#Variables
G=6.67**(-11) #Constante gravitacional
M=6*(10**12) #Masa de la tierra
dt= 0.01
r0=147 #Radio inicial a su vez semieje mayor de la elipse
theta0=0 #Angulo inicial
b=147 #Semieje menor de la elipse
f=(r0**2-b**2)**0.5 #Foco de la elipse
rLT = r0-f #Distancia Tierra luna inicial
r_o0=30
theta_o0=(r_o0**2)/rLT
pos0L=vector(r0,0,0) #Posicion inicial luna
pos0T=vector(0,0,0) #Posicion inicial tierra
rLT = r0 #Distancia Tierra luna inicial

#Figuras
	#Luna
luna=sphere(pos=pos0L,radius=r0/50,color=color.white,make_trail=True)
	#Tierra
tierra=sphere(pos=pos0T,radius=r0/40,color=color.green,make_trail=True)
	#Ejes de la cónica [Los nombres estan pensados en la izq del cuadrante]
eje1=arrow(axis=vector(r0+20,0,0),color=color.red,shaftwidth=0.05)
eje2=arrow(axis=vector(0,b+20,0),color=color.red,shaftwidth=0.05)
eje3=arrow(axis=-eje1.axis,color=color.red,shaftwidth=0.05)
eje4=arrow(axis=-eje2.axis,color=color.red,shaftwidth=0.05)
	#Vectores unitarios en polares de la luna [T=tongo]
thetaT=arrow(pos=luna.pos,axis=vector(0,luna.radius*5,0),color=color.orange)
txt_thetaT = text(text='Φ', pos=thetaT.pos + thetaT.axis, axis=thetaT.axis, align='center', height=0.8,
                color=color.white, billboard=True, emissive=True)
roT=arrow(pos=luna.pos,axis=vector(luna.radius*5,0,0),color=color.orange)
txt_ro = text(text='ρ', pos=roT.pos + roT.axis, axis=roT.axis, align='center', height=0.8,
                color=color.white, billboard=True, emissive=True)

#Movimiento
print(rLT)
while True :
	rate(100)
	#EDO
	r_oo= rLT*(theta_o0**2) + ((-G*M)/(rLT**2))
	theta_oo= ((-1)*2*r_o0*theta_o0)/rLT
	#Aproximaciones
	r_o= r_o0 + r_oo*dt
	r= rLT + r_o*dt
	theta_o= theta_o0 + theta_oo*dt
	theta= theta0 + theta_o*dt
	#Redefinimos para el sgte calculo
	r_o0= r_o
	theta_o0= theta_o
	rLT= r
	theta0= theta
	#Actualización de posiciones
	luna.pos=thetaT.pos=roT.pos=vector(r*np.cos(theta),r*np.sin(theta),0)
	thetaT.axis=vector(np.sin(theta),np.cos(theta),0)
	roT.axis=vector(np.cos(theta),np.sin(theta),0)


