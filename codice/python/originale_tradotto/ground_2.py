import scipy.integrate as solve_ivp
#from rkt_dyn import simulate_launch
import numpy as np



import math
import rocketmodel as rk
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

time_range = [0, 10]
initial_conditions = [(10, 0, 0), (0, 10, 3)]
time_evalpoints = np.arange(0., 10.01, 0.1) 

sol = solve_ivp(simulate_launch, time_range, initial_conditions)

print(sol.t)