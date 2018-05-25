from vpython import *
#Datos

G=6.67**(-11) #cte. gravitacion universal
M=10*10**10# masa planet kg (debe ser de ese orden para que el sistema se pueda mover
R=10 #radio planet mts
r=5.0  #radio moon mts
h=2.0  #distancia entre ambos cuerpos mts
theta=0  #angulo inicial
theta_punto=((G*M)/(R+h)**3.0)**(1.0/2.0) #velocidad angular sacada de la EDO
dt=0.01 #invervalos de tiempo


#objetos orbitando
planet=sphere(pos=vector(0,0,0),radius=R/10,color=color.blue)
moon=sphere(pos=vector(R+h,0,0),radius=r/10,color=color.white,make_trail=True)

# vectores unitarios
x_i=arrow(pos=vector(0,0,0),axis=vector(R*0.5,0,0),color=color.red,shaftwidth=0.05)
txt_x=text(text='i',pos=x_i.pos+x_i.axis,axis=x_i.axis,align='center',height=0.8,color=color.white,
           billboard=True, emissive=True)

y_j=arrow(pos=vector(0,0,0),axis=vector(0,R*0.5,0),color=color.yellow,shaftwidth=0.05)
txt_y=text(text='j',pos=y_j.pos+y_j.axis,axis=y_j.axis,align='center',height=0.8,color=color.white,
           billboard=True, emissive=True)

#vectores polares
p_r=arrow(pos=moon.pos,axis=vector(r*2,0,0),color=color.cyan)
txt_p = text(text='ρ', pos=p_r.pos + p_r.axis, axis=p_r.axis, align='center', height=0.4,
                color=color.white, billboard=True, emissive=True)

theta_o=arrow(pos=moon.pos,axis=vector(0,r*2,0),color=color.purple)
txt_theta = text(text='Φ', pos=theta_o.pos + theta_o.axis, axis=theta_o.axis, align='center', height=0.4,
                color=color.white, billboard=True, emissive=True)

#ecuacion de movimiento
while True:
    rate(100)
    #actualizacion mov satelite c/r al angulo
    moon.pos=vector(cos(theta),sin(theta),0)*(R+h)

    #actuaizacion posicion vectores polares
    p_r.pos=theta_o.pos=moon.pos

    #actualizacion direccion y sentido vectores polares
    p_r.axis=vector(cos(theta),sin(theta),0)
    theta_o.axis=vector(-sin(theta),cos(theta),0)

    #Letritas
    txt_p.pos=p_r.pos+p_r.axis
    txt_theta.pos=theta_o.pos+theta_o.axis

    theta=theta+theta_punto*dt

    #print de los angulos thetas que se genera mientras se mueve el satelite
    print(theta)











