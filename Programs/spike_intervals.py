import numpy as np

def extract_spikes(s,theta,t0=0.0,tmax=50.0,dt=0.001):
    Ti=[]
    t=t0

    val=-1
    while t<tmax:
        fire=False
        inte=0
        while fire==False:
            val += 1
            
            if val>len(s)-1:
                break
            
            inte += s[val]*dt
            t += dt
            
            
            if inte >= theta:
                Ti.append(t)
                fire=True
                
    ti=[(Ti[i+1]-Ti[i]) for i in range(len(Ti)-1)]
    return ti

def signal(x):
    s=[(i+2)**2 for i in x]
    return s

def read_x(equation='lorentz',initial_time=0.0,last_time=50.0,dt=0.001):
    x,y,z=[],[],[]
    file_name = '{}_{}_{}'.format(initial_time,last_time,dt)
    with open('data/{}/{}.dat'.format(equation,file_name), 'r') as f:
        for linea in f:
            value = linea.split(" ")
            value[2].split("/n")
            x.append(float(value[0]))
            y.append(float(value[1]))
            z.append(float(value[2]))
    return x,y,z

x,y,z=read_x()
s=signal(x)
ti=extract_spikes(s,20,0.001,50)

