%% Initialization
close all; clear all; clc
global g A cD Ap Isp th cDp rho tb td tT
%% Input parameters
% rocket
m0=0.3; % total mass [kg] range: 0.25 - 0.3 kg ; apogeo max: 200 m
A=pi/4*0.035^2; % rocket cross section [m^2]
cD=0.5; % drag coefficient [#]
Ap=0.8; % parachute area [m^2]
cDp=0.8; % drag coefficient [#]
% environment
g=9.81; % acceleration of gravity [m/s^2]
th_deg=85; % heading angle [deg]
rho=1.225; % air density [kg/m^3]
%% KLIMA D9-3;
    mp0=0.016; % propellant mass [kg]
    Itot=20; % total impulse [Ns]
    tT=[0 0; 0.1 9.2;0.2 25;0.3 15;0.4 10;0.5 9.2;0.6 9.2;0.8 9.2;0.9 9.2;1.7 9.2; 1.8 9; 1.9 8; 2.0 6.25; 2.1 3.75; 2.2 0]; % D9-3
    td=3;
%% KLIMA C6-3
%     mp0=0.01; % propellant mass [kg]
%     Itot=10; % total impulse [Ns]
%     tT=[0 0; 0.1 3; 0.2 8; 0.3 15;0.4 10;0.5 8;0.6 6.4;0.8 6.2;1.2 6.2;1.3 6.1; 1.4 5.2; 1.5 3.6; 1.7 0];
%     td=3;
%% KLIMA D12-3
%     mp0=0.021; % propellant mass [kg]
%     Itot=16.8; % total impulse [Ns]
%     tT(:,1)=[0 0.1 0.2 0.28 0.3 0.4 0.5 1.6 1.7];
%     tT(:,2)=[0 7.5 18 30 23 12 10.5 8 0];
%     td=3;
%% Parameters processing
dp=sqrt(4*Ap/pi); % parachute diameter [m]
Isp=Itot/mp0/g; % specific impulse [s]
ms=m0-mp0; % structure mass [kg]
tb=tT(end,1);
th=deg2rad(th_deg);
%% Processing
options = odeset('Events','ground_2','RelTol',1e-13,'AbsTol',1e-15);
[t X]=ode45(@rkt_dyn,[0 100],[0 0 0 0 m0],options);
x=X(:,1);
y=X(:,2);
vx=X(:,3);
vy=X(:,4);
m=X(:,5);
%% Representation
figure(1) 
plot(tT(:,1),tT(:,2))
xlabel('time [s]')
ylabel('thrust [N]')

figure(2)
plot(t,m*1000)
xlabel('time [s]')
ylabel('mass [g]')

figure(3)
hold on
plot(x,y)
xlabel('x [m]')
ylabel('y [m]')

figure(4)
hold on
plot(t,y)
plot(tb+td,interp1(t,y,tb+td),'o')

xlabel('t [s]')
ylabel('y [m]')

figure(5)
hold on
plot(t,vx)
plot(tb+td,interp1(t,vx,tb+td),'o')
xlabel('t [s]')
ylabel('vx [m/s]')

figure(6)
hold on
plot(t,vy)
plot(tb+td,interp1(t,vy,tb+td),'o')
xlabel('t [s]')
ylabel('vy [m/s]')

disp('d_p [m]')
disp(dp)
disp('x_max [m]')
disp(max(x))
disp('y_max [m]')
disp(max(y))
disp('tf [s]')
disp(t(end))
disp('Vyf [m/s]')
disp(vy(end))