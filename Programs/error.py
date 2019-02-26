import numpy as np 
from scipy.spatial import distance

def knn(vector_list, index, pc_clossest=1., pc_close_del=5):
    """vector_list must be of the type np.array([V0,V1,...,Vk]) with Vi = [ti,ti-1,ti-2]"""
    N = len(vector_list)
    n_del, n_close = int(N*pc_close_del/100.), int(N*pc_clossest/100.)
    D = distance.squareform(distance.pdist(vector_list))[index][n_del:] #Note that we delete the 0.5% that would be interpolation.
    v0_closest = np.argsort(D)[:n_close] 
    return (v0_closest+n_del) #1% closest - torna una array amb els index dels mes propers en ordre.


def neirest_pred(vector_list, index):
    close_index = knn(vector_list, index)
    k = len(close_index)
    pred = 0.0
    for i in range(k):
        if close_index[i] == len(vector_list)-1:
            pred += vector_list[close_index[i]-1][2]
        else:
            pred += vector_list[close_index[i]+1][2]
    return pred/k 


def npe(vector_list):
    m = np.sum(np.mean(vector_list, axis=0))/3.
    N = len(vector_list)
    num = 0.0
    denom = 0.0
    for i in range(N-1):
        t_real = vector_list[i+1][2]
        num += (neirest_pred(vector_list, i) - t_real)**2.
        denom += (m - t_real)**2.
    return np.sqrt(num/denom)


