import numpy as np 
import scipy.spatial import distance 


def neirest(vector_list):
    """vector_list must be of the type np.array([V0,V1,...,Vk]) with Vi = [ti,ti-1,ti-2]"""
    N = len(vector_list)
    D = distance.squareform(distance.pdist(vector_list))
    closest = np.argsort(D, axis=1)
    v0_closest = closest[0][int(N*0.001):] #Note that we delete the 0.1% that would be interpolation.
    

