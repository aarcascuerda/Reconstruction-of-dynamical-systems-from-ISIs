import numpy as np 
from scipy.spatial import distance 


def neirest(vector_list):
    """vector_list must be of the type np.array([V0,V1,...,Vk]) with Vi = [ti,ti-1,ti-2]"""
    N = len(vector_list)
    D = distance.squareform(distance.pdist(vector_list))[0][int(N*0.001):] #Note that we delete the 0.1% that would be interpolation.
    v0_closest = np.argsort(D) 
    return v0_closest[:int(N*0.01)] #1% closest - torna una array amb els index dels mes propers en ordre.



    


