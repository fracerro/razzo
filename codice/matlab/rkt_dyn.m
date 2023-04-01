function dX=rkt_dyn(t,X)
global g A cD Ap Isp th cDp rho tb td tT

x=X(1);
y=X(2);
vx=X(3);
vy=X(4);
m=X(5);

gamma=atan2(vy,vx);
v=sqrt(vx^2+vy^2);

if t<=tb+td
    D=0.5*rho*v^2*A*cD;
else
    D=0.5*rho*v^2*Ap*cDp; % exp opening
end

if t<=tb
    Ta=interp1(tT(:,1),tT(:,2),t);
    dm=-Ta/g/Isp;
else
    Ta=0;
    dm=0;
end

ax=Ta*cos(th)/m-D/m*cos(gamma);
ay=Ta*sin(th)/m-D/m*sin(gamma)-g;

dX(1,1)=vx;
dX(2,1)=vy;
dX(3,1)=ax;
dX(4,1)=ay;
dX(5,1)=dm;
