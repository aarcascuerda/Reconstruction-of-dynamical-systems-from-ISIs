import matplotlib.pyplot as plt


def extract_spikes(s,theta,t0,tmax,dt):
    Ti=[]
    t=t0

    val=-1
    while t<tmax-dt:
        fire=False
        inte=0
        while fire==False:
            val += 1
            
            if val>len(s)-1:
                break
            
            inte += s[val]*dt
            t += dt
            #print(t)
            
            if inte >= theta:
                Ti.append(t)
                fire=True
            if (len(Ti)-1)==1024:
                break
                
    ti=[(Ti[i+1]-Ti[i]) for i in range(len(Ti)-1)]
    return ti

def signal(x):
    s=[(i+2)**2 for i in x]    #lorentz
    #s=[(i+40) for i in x]    #rossler
    return s

def read_x(t0,tmax,dt,equation='lorentz'):
    x,y,z=[],[],[]
    file_name = '{}_{}_{}'.format(t0,tmax,dt)
    with open('data/{}/{}.dat'.format(equation,file_name), 'r') as f:
        for linea in f:
            value = linea.split(" ")
            value[2].split("/n")
            x.append(float(value[0]))
            y.append(float(value[1]))
            z.append(float(value[2]))
    return x,y,z

def writer_spikes(ti,equation='lorentz'):
    file_name=str(theta)+'_'+str(tmax)+'_'+str(dt)
    with open('data/{}/times/{}.dat'.format(equation,file_name), 'w') as file_obj:
        for i in range(len(ti)):
            file_obj.write('{}\n'.format(ti[i]))
        
            
def writer_spikes_space(ti,theta,t0,tmax,dt,equation='lorentz'):
    file_name=str(theta)+'_'+str(t0)+'_'+str(tmax)+'_'+str(dt)
    
    x=[ti[i] for i in range(len(ti)-2)]
    y=[ti[i+1] for i in range(len(ti)-2)]
    z=[ti[i+2]for i in range(len(ti)-2)]
    
    with open('data/{}/time_space/12series/{}.dat'.format(equation,file_name), 'w') as file_obj:
        for i in range(len(x)):
            file_obj.write('{} {} {}\n'.format(x[i],y[i],z[i]))

"""
#parameters for spikes intervals
theta=60
t0=0.
tmax=1000.
dt=0.001

#extraction of x
x,y,z=read_x(t0,tmax,dt)

t=[]
ti=0
dt=0.001
for i in range(len(x)):
    t.append(ti)
    ti += dt
plt.figure(1)
plt.ylabel("x")
plt.xlabel("t")
plt.plot(t,x)
plt.show()
"""

#create signal
#s=signal(x)


"""
#extract and write spikes intervals
ti=extract_spikes(s,theta,t0,tmax,dt)
#writer_spikes(ti)
writer_spikes_space(ti,theta,t0,tmax,dt)
"""