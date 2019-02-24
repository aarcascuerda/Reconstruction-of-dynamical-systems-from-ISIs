import numpy as np 
from scipy.spatial import distance 


def neirest(vector_list, pc_clossest=1., pc_close_del=1.):
    """vector_list must be of the type np.array([V0,V1,...,Vk]) with Vi = [ti,ti-1,ti-2]"""
    N = len(vector_list)
    n_del, n_close = int(N*pc_close_del/100.), int(N*pc_clossest/100.)
    D = distance.squareform(distance.pdist(vector_list))[0][n_del:] #Note that we delete the 0.1% that would be interpolation.
    v0_closest = np.argsort(D)[:n_close] 
    return (v0_closest+n_del) #1% closest - torna una array amb els index dels mes propers en ordre.



    


