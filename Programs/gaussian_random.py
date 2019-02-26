import numpy as np 

def gs_ran(vector_list):
    N = len(vector_list)
    nvl = np.zeros((N,3)) - 1.0
    k = 0
    while k < N:
        rand = int(np.random.normal(k,N))
        if rand > -1 and rand < 100 and nvl[rand][0] < 0.:
            nvl[rand] = vector_list[k]
            k += 1
            print(k)
    return nvl