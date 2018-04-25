from scipy.integrate import odeint
import numpy as np


def ec(y, t, m, g, r):
	theta, thetap = y
	thetapp = g*np.sin(theta)/r
	return [thetap, thetapp]


def soledo(y0, t, m, g, r):
	return odeint(ec, y0, t, args=(m,g,r))[:,0]
