import numpy as np
from scipy.spatial import distance
import numba as nb


def knn(vector_list, index, pc_clossest=1.0, pc_close_del=0.5):
    """vector_list must be of the type np.array([V0,V1,...,Vk]) with Vi = [ti,ti-1,ti-2]"""
    N = len(vector_list)
    n_del, n_close = int(N * pc_close_del / (2.0 * 100.0)), int(N * pc_clossest / 100.0)
    D = distance.squareform(distance.pdist(vector_list))[index]
    if index < n_del:
        a = n_del + index + 1
        b = 0
        close_list = D[a:]
        v0_closest = np.argsort(close_list) + a
    else:
        if index >= (N - n_del):
            a = 0
            b = index - n_del
            close_list = D[:b]
            v0_closest = np.argsort(close_list)
        else:
            a = index + n_del + 1
            b = index - n_del
            close_list = np.concatenate((D[:b], D[a:]), axis=None)
            v0_closest = np.argsort(close_list)
            v0_closest = check_loop(v0_closest, b, n_del)

    return v0_closest[:n_close]


@nb.njit
def check_loop(v0_closest, b, n_del):
    for i in range(len(v0_closest)):
        if v0_closest[i] >= b:
            v0_closest[i] += 2 * n_del + 1
    return v0_closest


def neirest_pred(vector_list, index):
    close_index = knn(vector_list, index)
    k = len(close_index)
    pred = 0.0
    for i in range(k):
        if close_index[i] == len(vector_list) - 1:
            pred += vector_list[close_index[i] - 1][2]
        else:
            pred += vector_list[close_index[i] + 1][2]
    return pred / k


def npe(vector_list):
    m = np.sum(np.mean(vector_list, axis=0)) / 3.0
    N = len(vector_list)
    num = 0.0
    denom = 0.0
    for i in range(N - 1):
        t_real = vector_list[i + 1][2]
        num += (neirest_pred(vector_list, i) - t_real) ** 2.0
        denom += (m - t_real) ** 2.0
    return np.sqrt(num / denom)

