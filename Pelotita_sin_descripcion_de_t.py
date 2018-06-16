from vpython import *
from soledo import soledo
import numpy as n

'''Datos del problema
****** ESCRIBIR DESCRIPCION 

Para la cinematica definiremos un MCU hasta theta=48,2°, pues en ese ángulo la normal se anula. Después será 
caída libre.

*******

masa particula           : m
Esfera que cae           : rE
Esfera por la que desliza: rA
posicion inicial         : y0
gravedad                 : g
tiempo                   : dt

'''

m=2 
rE=1 
rA=15 
g=9.8 
y0=[pi/100,0] 
dt=n.linspace(0,7,501)

#Lista de thetas y thetas punto jaja saludos
sol=soledo(y0,dt,m,g,rA)
T = sol[:,0] #Lista theta
Tp = sol[:,1] #lista theta punto
k = n.argmin(abs(m*(g*n.cos(T)-rA*(Tp**2)))) #indice del theta en el que se "anula" la normal
v0=vector(rA*n.cos(T[k])*Tp[k],-rA*n.sin(T[k])*Tp[k],0) #Velocidad al anularse la normal
r0=vector(rA*n.sin(T[k]),rA*n.cos(T[k]),0) #Posicion cuando se anula la normal

''' Ajustes pantalla '''
scene.width = 600
scene.height = 600
scene.forward = vector(0,-.30,-10)

#Declaración de objetos
e=sphere(pos=vector(0,rA,0), radius=rE, color=color.red,
	make_trail=True, trail_type="curve")
ruta=ring(pos=vector(0,0,0), axis=vector(0,0,1),radius=rA, thickness=0.1) #Por defecto será blanco
#Vectores de fuerza
	#Normal
normal=arrow(pos=e.pos, axis=vector(0,m*g,0),color=color.yellow, shaftwidth=0.1)

	#Peso
p=arrow(pos=e.pos, axis=vector(0,-m*g,0),color=color.orange, shaftwidth=0.1)

scene.autoscale = False

while True:
	normal.visible = True
	for i in range(len(T)):
		rate(60)
		if i<k: #MCU
			theta = T[i]
			omega = Tp[i]
			
			e.pos=normal.pos=p.pos=vector(rA*n.sin(theta),rA*n.cos(theta),0)
			normal.axis=m*(g*n.cos(theta)-rA*(omega**2))*vector(sin(theta),cos(theta),0)
			if not e.make_trail:
				e.make_trail = True
				e.clear_trail()
				 
		else:  #Caida libre
			if not e.make_trail: e.make_trail = True
			e.pos=p.pos=r0+v0*(dt[i]-dt[k])+0.5*((dt[i]-dt[k])**2)*vector(0,-g,0)
			normal.visible = False
	e.make_trail=False
	e.clear_trail()


