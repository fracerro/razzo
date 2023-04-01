#!/usr/bin/env python3

import math

# --- DICHIARAZIONE DELLE COSTANTI FISICHE ---

# accelerazione di gravità
g = 9.80419 # Bologna
# g = 9.80352 # Roma

m0 = 0.3 # total mass [Kg]
A = math.pi/(4*(0.035**2)) # rocket cross section [m^2]
cD = 0.5 # drag coefficient [#]
Ap = 0.8 # parachute area [m^2]
cDp = 0.8 # drag coefficient [#]
# environment
th_deg = 85 # heading angle [deg]
rho = 1.225 # air density [kg/m^3]
## KLIMA D9-3
mp0 = 0.016 # propellant mass [kg]
Itot = 20 # total impulse [Ns]
tT = [(0, 0), (0.1, 9.2), (0.2, 25), (0.3, 15), (0.4, 10), (0.5, 9.2), (0.6, 9.2), (0.8, 9.2), (0.9, 9.2), (1.7, 9.2), (1.8, 9), (1.9, 8), (2.0, 6.25), (2.1, 3.75), (2.2, 0)] # D9-3
td = 3
## KLIMA C6-3
#     mp0=0.01 # propellant mass [kg]
#     Itot=10 # total impulse [Ns]
#     tT=[0 0; 0.1 3; 0.2 8; 0.3 15;0.4 10;0.5 8;0.6 6.4;0.8 6.2;1.2 6.2;1.3 6.1; 1.4 5.2; 1.5 3.6; 1.7 0];
#     td=3
## KLIMA D12-3
#     mp0=0.021; # propellant mass [kg]
#     Itot=16.8; # total impulse [Ns]
#     tT(:,1)=[0 0.1 0.2 0.28 0.3 0.4 0.5 1.6 1.7];
#     tT(:,2)=[0 7.5 18 30 23 12 10.5 8 0];
#     td=3;
## Parameters processing
dp = math.sqrt(4*Ap/math.pi) # parachute diameter [m]
Isp = Itot/(mp0*g) # specific impulse [s]
ms = m0-mp0 # structure mass [kg]
tb = tT[-1]
th = math.radians(th_deg)

# --- PROCESSO DEI DATI --- 

# conviene usare scipy.integrate.solve_ivp per l'eq. differenziale