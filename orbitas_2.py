from vpython import *

'''Datos del problema
****** ESCRIBIR DESCRIPCION *******

Constante de gravitacion universal: G
radio planeta (Masa mayor)        : Rp
Masa mayor                        : M
radio satelite (Masa menor)       : rs
Radio de trayectoria              : r
Radio de tray 1 d                 : dr
angulo                            : theta
theta 1 derivada                  : dtheta
tiempo                            : dt

e = (a^2+b^2)**(0.5)/a
ea = c
e = c/a

'''

'''funcion que entrega lista de elementos de una elipse'''
# float float -> list
#L=[directriz, b, c]
def elipse(e,a):
  directriz = a/e - e*a
  b = pow(directriz - pow(a,2),0.5)
  c = pow(pow(a,2)+pow(b,2),0.5)
  return [directriz, b , c]

G=6.67**(-11)
M=6*10**12
e = 0.2
a = 30
L = elipse(e,a)
b = L[1]
Rp=50 
rs=10 
theta=0 
r_o=1/(((cos(theta)/a)**2)+((sin(theta)/b)**2))**0.5 
dtheta=((G*M)/(r_o)**3.0)**(1.0/2.0)
dt=0.01

#objetos orbitando
planet=sphere(pos=vector(f,0,0),radius=Rp/10,color=color.blue)
moon=sphere(pos=vector(a,0,0),radius=rs/10,color=color.white,maker_train=True)

#vectores unitarios centrales
x_i=arrow(pos=vector(0,0,0),axis=vector(a+10,0,0),color=color.red,shaftwidth=0.05)
txt_x=text(text='i',pos=x_i.pos+x_i.axis,axis=x_i.axis,align='center',height=1.5,color=color.white,
           billboard=True, emissive=True)
_x_i=arrow(pos=vector(0,0,0),axis=vector(-(a+10),0,0),color=color.red,shaftwidth=0.05)
txt_x_=text(text='-i',pos=_x_i.pos+_x_i.axis,axis=_x_i.axis,align='center',height=1.5,color=color.white,
           billboard=True, emissive=True)
y_j=arrow(pos=vector(0,0,0),axis=vector(0,b+10,0),color=color.yellow,shaftwidth=0.05)
txt_y=text(text='j',pos=y_j.pos+y_j.axis,axis=y_j.axis,align='center',height=1.5,color=color.white,
           billboard=True, emissive=True)
_y_j=arrow(pos=vector(0,0,0),axis=vector(0,-(b+10),0),color=color.yellow,shaftwidth=0.05)
txt_y_=text(text='j',pos=_y_j.pos+_y_j.axis,axis=_y_j.axis,align='center',height=1.5,color=color.white,
           billboard=True, emissive=True)

#semis_ejes
txt_a=text(text='a',pos=vector(a,0,0),axis=x_i.axis,align='center',height=1,color=color.white,
           billboard=True, emissive=True)
txt_a_=text(text='-a',pos=vector(-a,0,0),axis=x_i.axis,align='center',height=1,color=color.white,
           billboard=True, emissive=True)
txt_b=text(text='b',pos=vector(0,b,0),axis=y_j.axis,align='center',height=1,color=color.white,
           billboard=True, emissive=True)
txt_b_=text(text='-b',pos=vector(0,-b,0),axis=y_j.axis,align='center',height=1,color=color.white,
           billboard=True, emissive=True)
#vectores polares
p_r=arrow(pos=moon.pos,axis=vector(a/r,0,0),color=color.cyan)
txt_p = text(text='ρ', pos=p_r.pos + p_r.axis, axis=p_r.axis, align='center', height=0.8,
                color=color.white, billboard=True, emissive=True)

theta_o=arrow(pos=moon.pos,axis=vector(0,a/r,0),color=color.purple)
txt_theta = text(text='Φ', pos=theta_o.pos + theta_o.axis, axis=theta_o.axis, align='center', height=0.8,
                color=color.white, billboard=True, emissive=True)

#movimiento choro eliptico
while True:
    rate(100)
    #actualizacion r_o c/r al angulo theta
    r_o=(1/((((cos(theta)/a)**2)+((sin(theta)/b)**2))**0.5))

    #actualizacion mov satelite c/r al angulo
    moon.pos=vector(cos(theta),sin(theta),0)*r_o

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

    print(r_o) #print que confirma que el radio va cambiando c/r al angulo y forma una elipse bonita


