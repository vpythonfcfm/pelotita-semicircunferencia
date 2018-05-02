from vpython import *
import numpy as np
from math import *


#Parametros base
r = 4
beta = np.pi/4

scene.title = "<b>Pendulo</b></n>"

#Ajustamos tamaño de pantalla
scene.width = 640
scene.height = 600
scene.forward = vector(0,-.3,-1)

# Pendulo
Pen = sphere(pos=vector(r,0,0), radius=r/10, color=color.cyan,
    	make_trail=False, interval=1)


#Vectores unitarios
x_i = arrow(pos=vector(0,0,0), axis=vector(1,0,0), color=color.red, shaftwidth=0.05)
y_j = arrow(pos=vector(0,0,0), axis=vector(0,1,0), color=color.blue, shaftwidth=0.05)
z_k = arrow(pos=vector(0,0,0), axis=vector(0,0,1), color=color.green, shaftwidth=0.05)

# Vectores de trayectoria con sus respectivas letras
rarr = arrow(pos=Pen.pos, axis=vector(2*r,0,0), color=color.magenta, shaftwidth=0.08)
txt_rarr = text(text='ρ', pos=rarr.pos+rarr.axis, axis=rarr.axis, align='center', height=0.4,
          color=color.magenta, billboard=True, emissive=True)

tarr = arrow(pos=Pen.pos, axis=vector(0,1,0), color=color.white, shaftwidth=0.08)
txt_tarr = text(text='Φ', pos=tarr.pos+tarr.axis, axis=tarr.axis, align='center', height=0.4,
          color=color.white, billboard=True, emissive=True)

scene.autoscale = True


# aqui escribimos la descripcion del video
scene.append_to_caption("""Pendulo bajo la accion de la gravedad""")

dt=1.0/60 # intervalo de tiempo
ang=atan(1.0*Pen.pos.y/Pen.pos.x) #angulo
omega = 0.5 # velocidad angular inicial
theta=pi/4 # amplitud
n = 0 #contador

while True:

	rate(60)  # Espera 1/60 s para que no se vea tan rapido
	theta = theta + omega*dt
	
	if abs(omega)<0.008: # Para que el vector theta posea modulo, dirección, y sentido de omega
                n = n + 1

	# actualiza la direccion de r y theta
	rarr.axis = vector(cos(theta),sin(theta),0)
	tarr.axis = ((-1)**n)*cos(ang)*vector(-sin(theta),cos(theta), 0)

	# actualiza la direccion de r, theta y el pendulo
	rarr.pos = tarr.pos = Pen.pos = vector(r*cos(theta), r*sin(theta),
		0)
			
	#generamos las letras
	txt_rarr.pos = rarr.pos+rarr.axis
	txt_tarr.pos = tarr.pos+tarr.axis

	# cambio del angulo y omega
	ang = atan(1.0*Pen.pos.y/Pen.pos.x)
	omega = omega - (10.0/r)*sin(ang)*dt/2
	print (omega)
