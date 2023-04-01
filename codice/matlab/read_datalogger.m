%% Initialization 
clear all; close all; clc 
T = readtable("dataLog00169.TXT"); % input IMU data
%% Input parameters
accel_offset = 0*[-67.5394, 959.6972, -217.5486]; % [mg]
gyro_offset = 0*[-0.2258, 0.7314, -0.8506]; % [dps]
accel_fs = 10; % lpf accelerometer [Hz]
gyro_fs = 15; % lpf gyroscope [Hz]
t0=453; % initial time [s]
tf=459; % final time [s]
clr=[0.3 0.3 0.3]; % color of non-filtered data
%% Parameters processing
% IMU data sorting
accel_raw = T{:,{'aX','aY','aZ'}}; % [mg]
gyro_raw = T{:,{'gX','gY','gZ'}}; % [dps]
mag = T{:,{'mX','mY','mZ'}}; %[uT]
% IMU data correction
accel = accel_raw - accel_offset;
gyro = gyro_raw - gyro_offset;
% IMU data conversion
accel = accel/1000*9.81; % [m/s^2]
t = (T.micros - T.micros(1))*(1e-6); % time [s]
% IMU auxiliary variables
accel_norm = sqrt(sum(accel.*accel,2)); % acceleration norm [m/s^2]
fs=round(1/t(2)); % sampling frequency [Hz]
% IMU data filtering
[b_accel,a_accel] = butter(9,accel_fs/fs); % design order 9 Butterworth filter accelerometer
[b_gyro,a_gyro] = butter(9,gyro_fs/fs); % design order 9 Butterworth filter accelerometer
accel_f = filtfilt(b_accel,a_accel,accel);
accel_norm_f = filtfilt(b_accel,a_accel,accel_norm);
gyro_f = filtfilt(b_gyro,a_gyro,gyro);

%% Figures
figure(1)
hold on
plot(t,accel_f(:,1),'r','LineWidth',3)
plot(t,accel(:,1),'.-','MarkerSize',1,'Color',clr)
xlabel('t [s]')
ylabel('a_x [m/s^2]')
xlim([t0 tf])
legend('filtered','raw')
%
figure(2)
hold on
plot(t,accel_f(:,2),'g','LineWidth',3)
plot(t,accel(:,2),'.-','MarkerSize',1,'Color',clr)
xlabel('t [s]')
ylabel('a_y [m/s^2]')
xlim([t0 tf])
legend('filtered','raw')
%
figure(3)
hold on
plot(t,accel_f(:,3),'b','LineWidth',3)
plot(t,accel(:,3),'.-','MarkerSize',1,'Color',clr)
xlabel('t [s]')
ylabel('a_z [m/s^2]')
xlim([t0 tf])
legend('filtered','raw')
%
figure(4)
hold on
plot(t,accel_norm_f,'b','LineWidth',3)
plot(t,accel_norm,'.-','MarkerSize',1,'Color',clr)
xlabel('t [s]')
ylabel('|a| [m/s^2]')
xlim([t0 tf])
legend('filtered','raw')
%
figure(5)
hold on
plot(t,gyro_f(:,1),'r','LineWidth',3)
plot(t,gyro(:,1),'.-','MarkerSize',1,'Color',clr)
xlabel('t [s]')
ylabel('\omega_x [deg/s]')
xlim([t0 tf])
legend('filtered','raw')
%
figure(6)
hold on
plot(t,gyro_f(:,2),'g','LineWidth',3)
plot(t,gyro(:,2),'.-','MarkerSize',1,'Color',[0.7 0.7 0.7])
xlabel('t [s]')
ylabel('\omega_y [deg/s]')
xlim([t0 tf])
legend('filtered','raw')
%
figure(7)
hold on
plot(t,gyro_f(:,3),'b','LineWidth',3)
plot(t,gyro(:,3),'.-','MarkerSize',1,'Color',clr)
xlabel('t [s]')
ylabel('\omega_z [deg/s]')
xlim([t0 tf])
legend('filtered','raw')