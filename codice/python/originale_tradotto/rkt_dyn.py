import numpy as np
import scipy.integrate as solve_ivp
import math, scipy

import rocketmodel as rk

# APPUNTI:
# gamma è l'angolo di inclinazione con l'orizzontale
# primva versione: copia brainless del codice originale
#
#
#
#

# vars:

def simulate_launch(t, vars):
    (m, x, y) = vars[0]
    (m_dot, x_dot, y_dot) = vars[1]
    
    gamma = math.atan2(y_dot, x_dot)
    v = math.sqrt(x_dot * x_dot + y_dot * y_dot)

    if t <= rk.tb + rk.td:
        D = 0.5 * rk.rho * v * v * rk.A * rk.cD
    else:
        D = 0.5 * rk.rho * v * v * rk.Ap * rk.cDp # exp opening (qualsiasi cosa sia)
    
    if t <= rk.tb:
        Ta = f(scipy.interp1d(rk.tT[:,1], rk.tT[:,2], kind = 'cubic'), t)
        rk.dm -=Ta/rk.g/rk.Isp
    else:
        Ta = 0
        rk.dm = 0

    ax = Ta * math.cos(rk.th) / m - D / m * math.cos(gamma);
    ay = Ta * math.sin(rk.th) / m - D / m * math.sin(gamma) - g;
    
    return [vars[1], (0., ax, ay)]