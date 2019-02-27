import matplotlib.pyplot as plt
from error import knn, neirest_pred, npe
from gaussian_random import gs_ran
import numpy as np
from distributions import hist
from spike_intervals import read_space,read_spikes


#parameters for spikes intervals
t0=0.
tmax=2000.
dt=0.0001

npes=[]
npes_ran=[]
thetas=[]

theta_i=53.
theta_f=97.
incremento=(theta_f-theta_i)/11.
for i in range(12):
    theta=theta_i+i*incremento
    ti=read_spikes(theta,t0,tmax,dt)
    vector=np.array(read_space(theta,t0,tmax,dt))
    print("%i, theta=%.2f"%(i,theta))
    val=npe(vector)
    print("NPE=%.4f"%val)
    surrogate=gs_ran(vector)
    ti_surrogate=[surrogate[i][0] for i in range(len(surrogate))]
    valran=npe(surrogate)
    print("NPE_ran=%.4f"%valran)
    npes.append(val)
    npes_ran.append(valran)
    thetas.append(theta)
    
    pos,alt,err=hist(ti,10)
    plt.figure(i+10)
    plt.ylabel("P(ti)")
    plt.xlabel("ti")
    plt.plot(pos,alt)
    plt.show()
    
    pos2,alt2,err2=hist(ti_surrogate,10)
    plt.figure(i+10)
    plt.ylabel("P(ti)")
    plt.xlabel("ti")
    plt.plot(pos2,alt2)
    plt.show()

plt.figure(1)
plt.ylim(0,1.2)
plt.ylabel("NPE")
plt.xlabel("threshold")
plt.plot(thetas,npes)
plt.plot(thetas,npes_ran)
plt.show()