import os
import numpy as np
import matplotlib.pyplot as plt

data = []
with open("/run/media/kekko/dati/dataLog00012.TXT", "r") as auto:
    first = True
    for line in auto:
        if first:
            first = False
            continue
        data.append([line.split(",")[1:4], line.split(",")[4:7], line.split(",")[7:10], line.split(",")[-2]]) #accellerazione, giroscopio, magnetometro

# risolvo il problema di Cauchy:
# a(t) nota
# v(0) = 0
# r(0) = 0

# print(data)

fig = plt.figure()
ax = plt.axes(projection='3d')

px = []
py = []
pz = []

v = np.zeros(3)
r = np.zeros(3)
for sample in data:
    a = np.array([float(sample[0][0]), float(sample[0][1]), float(sample[0][2])])
    a /= 1000
    if (float(sample[3]) == 0):
        continue
    dt = 1 / float(sample[3])
    v += a * dt
    r += v * dt

    px.append(r[0])
    py.append(r[1])
    pz.append(r[2])

    dt = (ts - last_ts_gyro) / 1000
        last_ts_gyro = ts
        gyro_angle_x = gyro[0] * dt
        gyro_angle_y = gyro[1] * dt
        gyro_angle_z = gyro[2] * dt

        if firstGyro:
            total_x = gyro_angle_x
            total_y = gyro_angle_y
            total_z = gyro_angle_z
            firstGyro = False

        # totals
        total_x += gyro_angle_x
        total_y += gyro_angle_y
        total_z += gyro_angle_z

        # rad = > degree
        dtotal_x = np.rad2deg(total_x) % 360
        dtotal_y = np.rad2deg(total_y) % 360
        dtotal_z = np.rad2deg(total_z) % 360

        # rotation matrix
        Qx = np.array(
            [[1, 0, 0], [0, np.cos(dtotal_x[0]), -np.sin(dtotal_x[0])], [0, np.sin(dtotal_x[0]), np.cos(dtotal_x[0])]])
        Qy = np.array(
            [[np.cos(dtotal_y[0]), 0, np.sin(dtotal_y[0])], [0, 1, 0], [-np.sin(dtotal_y[0]), 0, np.cos(dtotal_y[0])]])
        Qz = np.array(
            [[np.cos(dtotal_z[0]), -np.sin(dtotal_z[0]), 0], [np.sin(dtotal_z[0]), np.cos(dtotal_z[0]), 0], [0, 0, 1]])
        Qxyz = Qx@Qy@Qz

        # a -Qxyz*g to filter out gravity
        g = np.array([[0], [0], [gravity_norm]])
        rotated_g = Qxyz @ g
        accelwithoutg = np.subtract(accelwithg, rotated_g)


    

ax.scatter(px, py, pz, color='red', s=1, marker='o')
plt.show()
