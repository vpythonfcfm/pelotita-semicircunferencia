from vpython import *
#Datos

G=6.67**(-11) #cte. gravitacion universal
M=6*10**12# masa planet kg (debe ser de ese orden para que el sistema se pueda mover
a=30   #semieje mayor
b=15   #semieje menor
f=10   #foco donde esta el planeta
R=50 #radio planet mts
r=10  #radio moon mts
theta=0  #angulo inicial
r_o=1/(((cos(theta)/a)**2)+((sin(theta)/b)**2))**0.5 #ecuacion de la elipse en coordenadas polares
theta_punto=((G*M)/(r_o)**3.0)**(1.0/2.0) #velocidad angular sacada de la EDO
dt=0.01 #invervalos de tiempo



#objetos orbitando
planet=sphere(pos=vector(f,0,0),radius=R/10,color=color.blue)
moon=sphere(pos=vector(a,0,0),radius=r/10,color=color.white,maker_train=True)

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
    theta=theta+theta_punto*dt

    print(r_o) #print que confirma que el radio va cambiando c/r al angulo y forma una elipse bonita


