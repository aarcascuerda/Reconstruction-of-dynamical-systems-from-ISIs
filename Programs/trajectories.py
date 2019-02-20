import numpy as np
import numba as nb
from scipy.integrate import odeint


class Functions:
    @staticmethod
    @nb.njit
    def lorentz(x_ini, t0, sigma=10., beta=8./3, rho=28.0):
        x = x_ini[0]
        y = x_ini[1]
        z = x_ini[2]
        return [sigma * (y - x), x * (rho - z) - y, x * y - beta * z]


class TrajectoryCalcul:

    function_def = "lorentz"
    time_interval_def = [0., 50.]
    initial_conditions_def = [-10., -10., -10.]
    dt_def = 0.001

    def __init__(
        self, function=None, time_interval=None, initial_conditions=None, dt=None
    ):
        self.function_name = function or self.function_def
        self.time_interval = time_interval or self.time_interval_def
        self.initial_conditions = initial_conditions or self.initial_conditions_def
        self.dt = dt or self.dt_def

    def eval_points(self):
        steps = int((self.time_interval[1] - self.time_interval[0]) / self.dt)
        return np.array([self.time_interval[0] + i * self.dt for i in range(steps)])

    def solution(self):
        return odeint(
            getattr(Functions, self.function_name),
            self.initial_conditions,
            self.eval_points(),
        )

class TrajectoryWriter:
    traj = TrajectoryCalcul()
    dir_name = traj.function_name
    solution = traj.solution()
    y = solution

    file_name = str(traj.time_interval[0])+'_'+str(traj.time_interval[1])+'_'+str(traj.dt)

    with open('data/{}/{}.dat'.format(dir_name,file_name), 'w') as file_obj:
        for i in range(len(y)):
            file_obj.write('{} {} {}\n'.format(y[i][0],y[i][1],y[i][2]))
