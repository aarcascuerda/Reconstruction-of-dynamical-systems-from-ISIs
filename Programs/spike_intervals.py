import numpy as np

def extract_spikes(s,theta,dt,tmax):
    Ti=[]
    t=0.
    
    for i in range(len(s)):
        fire=False
        inte=0
        while fire==False:
            inte += s[i]*dt
            t += t+dt
            if inte >= theta:
                Ti.append(t)
                fire=True
                
    ti=[(Ti[i+1]-Ti[i]) for i in range(len(Ti)-1)]
    
    
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
    