from vpython import *
from math import *
import numpy as np

'''Datos del problema

Constante de gravitacion universal  : G
Radio Cuerpo masa mayor             : Cmayor
Masa mayor                          : M
Radio Cuerpo masa menor             : Cmenor
Vector trayectoria                  : r
Vector trayectoria, primera derivada: dr
angulo                              : theta
theta 1 derivada                    : dtheta
tiempo                              : dt
excentricidad                       : e
semiejemayor                        : a

'''
running = True

def Run(b):
    global running
    running = not running
    if running: b.text = "Pause"
    else: b.text = "Run"

button(text="Pause", pos=scene.title_anchor, bind=Run)


# float float -> list
# devuelve lista de elementos de una elipse
# L=[directriz, b, c]
def elipse(e,a):
  directriz = a/e - e*a
  dif = abs((e*a)**2-a**2)
  f = e*a
  b = dif**0.5
  c = (a**2+b**2)**0.5
  return [directriz, b , c, f]

# unitarios de elipse: +-1 str str -> arrow
def unitarios(signo, eje, a, b):
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
  title = text(text= texto, pos=flecha.pos+flecha.axis, axis = flecha.axis, 
              align = 'center', height = altura, color = color.white,
              billboard = True, emissive = True)
  return title

G        =6.7e-11
M        = 30e12
e        = 0.8
a        = 30
c_elipse = elipse(e,a)
CRmayor  =20 
CRmenor  =10 
theta    =0
r        = a*(1-pow(e,2))/(1-e*cos(theta))
dtheta   =(G*M/pow(r,3))**(0.5)
dt       =0.001

#objetos orbitando
sol=sphere(pos=vector(-c_elipse[3],0,0),radius=CRmayor/10,color=color.yellow)

planet=sphere(pos=vector(r*cos(theta)-c_elipse[3],r*sin(theta),0),radius=CRmenor/10,
              color=color.orange,make_trail=True,trail_type='points', interval=4)

#vectores unitarios centrales
x_i = unitarios(1,"x",a,c_elipse[1])
_x_i = unitarios(-1,"x",a,c_elipse[1])
y_j = unitarios(1,"y",a,c_elipse[1])
_y_j = unitarios(-1,"y",a,c_elipse[1])

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
txt_b.pos = vector(0,c_elipse[1],0)
txt_b_=textVector('-b',x_i,1.0)
txt_b_.pos = vector(0,-c_elipse[1],0)

#vectores polares
rho=arrow(pos=planet.pos,axis=vector(cos(theta),sin(theta),0),color=color.cyan,shaftwidth = 0.1)
txt_rho = textVector('P',rho,1)

dthetaFlecha=arrow(pos=planet.pos,axis=vector(-sin(theta),cos(theta),0),color=color.red,shaftwidth = 0.1)
txt_dtheta = textVector('0',dthetaFlecha,1)

scene.caption = "\nVariacion en el valor de la excentricidad: \n\n"

def setspeed(s):
    wt.text = '{:1.2f}'.format(s.value)
    
sl = slider(min=0.3, max=3, value=dtheta, length=220, bind=setspeed, right=15)
wt = wtext(text='{:1.2f}'.format(sl.value))
scene.append_to_caption(' -- (0 < e < 1)\n')

#movimiento choro eliptico
while True:
    rate(2000)
    #actualizacion dr c/r al angulo theta
    if running:
      r = a*(1-pow(e,2))/(1-e*cos(theta))
      #actualizacion mov satelite c/r al angulo
      planet.pos=vector(r*cos(theta)-c_elipse[3],r*sin(theta),0)

      #actualizacion direccion y sentido vectores polares
      rho.axis = vector(cos(theta), sin(theta), 0)*5
      dthetaFlecha.axis = vector(-sin(theta), cos(theta), 0)*5

      #actualizacion posicion vectores polares
      rho.pos = dthetaFlecha.pos = planet.pos
      #Letritas
      txt_rho.pos = rho.pos + rho.axis
      txt_dtheta.pos = dthetaFlecha.pos + dthetaFlecha.axis

      #cambio angulo theha
      theta=theta+sl.value*dt