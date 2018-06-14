from vpython import *
import numpy as np

'''Datos del problema
****** ESCRIBIR DESCRIPCION *******

Constante de gravitacion universal: G
Cuerpo masa mayor       : Cmayor
Masa mayor                        : M
Cuerpo masa menor      : Cmenor
Radio de trayectoria              : r
Radio de tray 1 d                 : dr
angulo                            : theta
theta 1 derivada                  : dtheta
tiempo                            : dt
excentricidad                     : e
semiejemayor                      : a


'''
# float float -> list
# devuelve lista de elementos de una elipse
# L=[directriz, b, c]
def elipse(e,a):
  directriz = a/e - e*a
  dif = pow(abs(pow(e*a,2)-pow(a,2)),0.5)
  b = pow(dif ,0.5)
  c = pow(pow(a,2)+pow(b,2),0.5)
  return [directriz, b , c]

# unitarios: +-1 str str -> arrow
def unitarios(signo, eje):
  vect = arrow()
  vect.pos = vector(0,0,0)
  vect.shaftwidth = 0.05
  if (abs(signo)==signo):
    if (eje == "x"):
      vect.axis = vector(a+10,0,0)
      vect.color = color.red
    elif (eje == "y"):
      vect.axis = vector(0,b+10,0)
      vect.color = color.yellow
  else:
    if(eje == "x"):
      vect.axis = vector(-(a+10),0,0)
      vect.color = color.red
    elif (eje == "y"):
      vect.axis = vector(0,-(b+10),0)
      vect.color = color.yellow
  return vect

def textVector(texto, flecha, altura):
  title = text(text= texto, pos=flecha.pos+flecha.axis, axis = flecha.axis, align = 'center', height = altura, color = color.white,
              billboard = True, emissive = True)
  return title

running = True

def Run(b):
    global running
    running = not running
    if running: b.text = "Pause"
    else: b.text = "Run"

button(text="Pause", pos=scene.title_anchor, bind=Run)

G=6.67**(-11)
M=6*10**12
e = 0.5
a = 30
L = elipse(e,a)
b = L[1]
f = e*a
Cmayor=20 
Cmenor=10 
theta=0 
r = a*(1-pow(e,2))/(1+3*cos(theta))
momentum = pow(r,2)
dr=a*(1)

dtheta=((G*M)/(dr)**3.0)**(1.0/2.0)
dt=0.01

#objetos orbitando
planet=sphere(pos=vector(f,0,0),radius=Cmayor/10,color=color.blue)
moon=sphere(pos=vector(a,0,0),radius=Cmenor/10,color=color.white,maker_train=True)

#vectores unitarios centrales
x_i = unitarios(1,"x")
_x_i = unitarios(-1,"x")
y_j = unitarios(1,"y")
_y_j = unitarios(-1,"y")

#text unitarios
txt_x = textVector('i',x_i,1.5)
txt_x_= textVector('-i',_x_i,1.5)
txt_y=textVector('j',y_j,1.5)
txt_y_=textVector('-j',_y_j,1.5)

#text semiejes
txt_a=textVector('a',x_i,1.0)
txt_a.pos = vector(a,0,0)
txt_a_=textVector('-a',x_i,1.0)
txt_a_.pos = vector(-a,0,0)
txt_b=textVector('b',x_i,1.0)
txt_b.pos = vector(0,b,0)
txt_b_=textVector('-b',x_i,1.0)
txt_b_.pos = vector(0,-b,0)

#vectores polares
p_r=arrow(pos=moon.pos,axis=vector(a/r,0,0),color=color.cyan)
txt_p = textVector('ρ',p_r,0.8)

theta_o=arrow(pos=moon.pos,axis=vector(0,a/r,0),color=color.red)
txt_theta = textVector('Φ',theta_o,0.8)

#movimiento choro eliptico
while True:
    rate(200)
    #actualizacion dr c/r al angulo theta
    if running:
      dr=(1/((((cos(theta)/a)**2)+((sin(theta)/b)**2))**0.5))

      #actualizacion mov satelite c/r al angulo
      moon.pos=vector(cos(theta),sin(theta),0)*dr

      #actualizacion direccion y sentido vectores polares
      p_r.axis = vector(cos(theta), sin(theta), 0)*(r/2)
      theta_o.axis = vector(-sin(theta), cos(theta), 0)*(r/2)

      #actualizacion posicion vectores polares
      p_r.pos = theta_o.pos = moon.pos
      #Letritas
      txt_p.pos = p_r.pos + p_r.axis
      txt_theta.pos = theta_o.pos + theta_o.axis

      #cambio angulo theha
      theta=theta+dtheta*dt
    
        