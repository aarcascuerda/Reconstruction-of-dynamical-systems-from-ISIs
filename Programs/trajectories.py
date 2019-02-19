import numpy as np 
import numba as nb
from scipy.integrate import solve_ivp


class functions:
    @staticmethod
    @nb.njit
    def lorentz(t, x, sigma=10, rho=28, beta=8/3):
        x[0] = sigma*(x[1]-x[0])
        x[1] = rho*x[0]-x[1]-x[0]*x[2]
        x[2] = -beta*x[2]+x[0]*x[1]
        return x


class TrajectoryWriter:

    function_def = 'lorentz'
    time_interval_def = np.array([0,100])
    initial_conditions_def = np.array([0.1,0.1,0.1])

    def __init__(self, function=None, time_interval=None, initial_conditions=None):
        self.function_name = function or self.function_def
        self.time_interval = time_interval or self.time_interval_def
        self.initial_conditions = initial_conditions or self.initial_conditions_def
    
    def solution(self):
        return solve_ivp(getattr(functions, self.function_name), self.time_interval, self.initial_conditions)

