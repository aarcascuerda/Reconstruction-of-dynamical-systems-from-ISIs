import matplotlib.pyplot as plt
from error import knn, neirest_pred, npe


def read_incs(ti,theta,tmax,dt,equation='lorentz'):
    vector=[ [] for i in range(12) ]
    theta_i=53.
    theta_f=97.
    incremento=(theta_f-theta_i)/11.
    for i in range(12):
        theta=theta_i+i*incremento
        file_name=str(theta)+'_'+str(t0)+'_'+str(tmax)+'_'+str(dt)

        with open('data/{}/time_space/12series/{}.dat'.format(equation,file_name), 'r') as f:
            for linea in f:
                value = linea.split(" ")
                value[2].split("/n")
                vector[i].append([float(value[0]),float(value[1]),float(value[2])])
    
    return xyz

#parameters for spikes intervals
t0=0.
tmax=2000.
dt=0.001
