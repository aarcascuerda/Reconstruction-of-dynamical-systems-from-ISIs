import numpy as np 
import numba as nb 

def gs_ran(vector_list):
    N = len(vector_list)
    nvl = np.zeros((N,3)) - 1.0
    k = 0
    while k < N:
        rand = int(np.random.normal(k,N))
        if rand > 0 and rand < 100 and nvl[rand][0] < 0.:
            nvl[rand] = vector_list[k]
            k += 1
            print(k)
    return nvl