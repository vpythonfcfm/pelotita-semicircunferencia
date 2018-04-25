from vpython import *
from soledo import soledo
import numpy as n

#Declaración de variables
m=2 #Kg
rE=1 #Esfera que cae
rA=15 #Esfera por la que desliza
g=9.8 #m/s^2
y0=[pi/100,0]
t=n.linspace(0,7,501)
#Lista de thetas jaja saludos
sol=soledo(y0,t,m,g,rA)
T = sol[:,0]
Tp = sol[:,1]
k = n.argmin(abs(m*(g*n.cos(T)-rA*(Tp**2)))) #indice
print(k)
v0=vector(rA*n.cos(T[k])*Tp[k],-rA*n.sin(T[k])*Tp[k],0)
r0=vector(rA*n.sin(T[k]),rA*n.cos(T[k]),0)

############Definicion del escenario

scene.width = 600
scene.height = 600
scene.forward = vector(0,-.30,-10)
############Definicion del escenario

#Declaración de objetos
e=sphere(pos=vector(0,rA+rE,0), radius=rE, color=color.red)
ruta=ring(pos=vector(0,0,0), axis=vector(0,0,1),radius=rA, thickness=0.1) #Por defecto será blanco
#Vectores de fuerza
	#Normal
normal=arrow(pos=e.pos, axis=vector(0,m*g,0),color=color.yellow, shaftwidth=0.1)

	#Peso
p=arrow(pos=e.pos, axis=vector(0,-m*g,0),color=color.orange, shaftwidth=0.1)

#Para la cinematica definiremos un MCU hasta theta=48,2°, pues en ese ángulo la normal se anula. Después será 
# caída libre con v_o=-2*g*rA*(1/3) ARREGLAR

scene.autoscale = False

while True:
	normal.visible = True
	for i in range(len(T)):
		rate(60)
		if i<k:
			theta = T[i]
			omega = Tp[i]
			
			e.pos=normal.pos=p.pos=vector(rA*n.sin(theta),rA*n.cos(theta),0)
			normal.axis=m*(g*n.cos(theta)-rA*(omega**2))*vector(sin(theta),cos(theta),0)
		
		else: #Viaja en el tiempo PROBLEMA
			e.pos=p.pos=r0+v0*(t[i]-t[k])+0.5*((t[i]-t[k])**2)*vector(0,-g,0)
			normal.visible = False


