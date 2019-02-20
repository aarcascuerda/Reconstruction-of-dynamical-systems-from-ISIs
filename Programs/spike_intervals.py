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
                
def read_x(texto):
    x,y,z=[],[],[]
    with open() as f:
        for linea in f:
            value = linea.split(" ")
            value[2].split("/n")
            x.append(float(value[0]))
            y.append(float(value[1]))
            z.append(float(value[2]))
    return x,y,z
    