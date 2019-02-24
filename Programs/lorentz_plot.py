from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt


def read_t(theta,t0,tmax,dt,equation='lorentz'):
    x,y,z=[],[],[]
    file_name=str(theta)+'_'+str(t0)+'_'+str(tmax)+'_'+str(dt)

    with open('data/{}/time_space/{}.dat'.format(equation,file_name), 'r') as f:
        for linea in f:
            value = linea.split(" ")
            value[2].split("/n")
            x.append(float(value[0]))
            y.append(float(value[1]))
            z.append(float(value[2]))
    return x,y,z

#parameters for spikes intervals
theta=60
t0=0.
tmax=1000.
dt=0.001

x,y,z=read_t(theta,t0,tmax,dt,equation='lorentz')

print(len(x))

fig = plt.figure()
ax = fig.gca(projection='3d')

ax.plot(x, y, z)
#ax.legend()

plt.show()

plt.figure(1)
plt.ylabel("x")
plt.xlabel("z")
plt.plot(x,z,'.')
plt.show()


t=[]
ti=0
for i in range(len(x)):
    t.append(ti)
    ti += dt
    
plt.figure(1)
plt.ylabel("x")
plt.xlabel("t")
plt.plot(t,x)
plt.show()
    