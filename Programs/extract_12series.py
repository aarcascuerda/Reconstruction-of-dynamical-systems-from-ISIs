import matplotlib.pyplot as plt
from spike_intervals import extract_spikes,signal,read_x,writer_spikes_space


#parameters for spikes intervals
t0=0.
tmax=2000.
dt=0.001

#extraction of x
x,y,z=read_x(t0,tmax,dt)

#create signal
s=signal(x)

#varying theta
theta_i=53.
theta_f=97.
incremento=(theta_f-theta_i)/11.
for i in range(12):
    theta=theta_i+i*incremento
    ti=extract_spikes(s,theta,t0,tmax,dt)
    print("len(ti)=%i para theta=%.4f"%(len(ti),theta))
    writer_spikes_space(ti,theta,t0,tmax,dt)
