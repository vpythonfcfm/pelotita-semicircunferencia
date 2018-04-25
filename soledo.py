from scipy.integrate import odeint
import numpy as np


def ec(y, t, m, g, r):
	theta, thetap = y
	thetapp = g*np.sin(theta)/r
	return [thetap, thetapp]


def soledo(y0, t, m, g, r):
	'''
	Resuelve la ecuacion diferencial de la pelotita y devuelve
	theta para cada instante t
	y0: vector de condiciones iniciales: [theta0, thetapunto0]
	t: vector con el tiempo (se recomienda numpy.linspace)
	m: masa de la pelotita
	g: aceleracion de gravedad
	r: radio de la semiesfera

	Ejemplo: theta = soledo([0.001,0],
							np.linspace(0,10,101),
							1,
							9.8,
							1)
	Nota: si las condiciones iniciales son [0,0], la pelotita
	no se va a mover, quedara en reposo sobre la punta de la
	semiesfera
	'''
	return odeint(ec, y0, t, args=(m,g,r))[:,0]
