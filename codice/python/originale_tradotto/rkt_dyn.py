import numpy as np
import scipy.integrate as solve_ivp
import math

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

    if t <= rk.tb + tk.td:
        D = 0.5 * rk.rho * v * v * rk.A * rk.cD
    else:
        D = 0.5 * rk.rho * v * v * rk.Ap * rk.cDp # exp opening (qualsiasi cosa sia)
    
    if t <= tb:
        # aggiustare la massa con interpolazione
        pass
    else:
        # altra roba
        pass

    ax = Ta * cos(th) / m - D / m * cos(gamma);
    ay = Ta * sin(th) / m - D / m * sin(gamma) - g;
    
    return [vars[1], (0., ax, ay)]