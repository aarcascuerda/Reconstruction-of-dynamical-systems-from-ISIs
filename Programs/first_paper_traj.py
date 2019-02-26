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
    
    def rossler(x_ini,t0,a=0.1,b=0.1,c=14):
        x = x_ini[0]
        y = x_ini[1]
        z = x_ini[2]
        return [-(y + z), x + a * y, b + z * ( x - c )]


class TrajectoryCalcul:

    function_def = 'rossler'
    time_interval_def = [0., 200.]
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

    def velocities(self):
        length = len(self.eval_points())
        vel = np.zeros((length))
        y = self.solution()
        for i in range(length):
            vel[i] = Functions.rossler(y[i],0.)[0]
        return vel

class TrajectoryWriter:

    def __init__(self):
        self.traj = TrajectoryCalcul()
        self.dir_name = self.traj.function_name
        self.solution = self.traj.solution()
        self.y = self.solution
        self.y_prima = self.traj.velocities()
        self.file_name = str(self.traj.time_interval[0])+'_'+str(self.traj.time_interval[1])+'_'+str(self.traj.dt)

    def writer(self):
        with open('data/first_paper/{}/{}.dat'.format(self.dir_name,self.file_name), 'w') as file_obj:
            for i in range(len(self.y)):
                file_obj.write('{} {}\n'.format(self.y[i][0],self.y_prima[i]))

    def writer_2(self):
        with open('data/first_paper/{}/{}_2.dat'.format(self.dir_name,self.file_name), 'w') as file_obj:
            for i in range(len(self.y)-100):
                file_obj.write('{} {}\n'.format(self.y[i][0],self.y[i+100][0]))