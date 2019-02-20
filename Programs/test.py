import numpy as np
from scipy import integrate
from trajectories import Functions
# Note: t0 is required for the odeint function, though it's not used here.
def lorentz_deriv(a, t0, sigma=10., beta=8./3, rho=28.0):
    x = a[0]
    y = a[1]
    z = a[2]
    return [sigma * (y - x), x * (rho - z) - y, x * y - beta * z]

x0 = [-10, -10, -10]  # starting vector
t = np.linspace(0, 50, 100000)  # one thousand time steps
x_t = integrate.odeint(Functions.lorentz, x0, t)
print(x_t)