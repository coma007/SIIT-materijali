import numpy as np
import matplotlib.pyplot as plt
import math

def newtonRaphson(x0,tol):
    x_novo = x0;
    x_pre = math.inf
    iter = 0
    while (abs(x_pre-x_novo) > tol):
        iter += 1
        x_pre = x_novo
        x_novo = x_pre-dfunc(x_pre)/ddfunc(x_pre)

    xopt = x_novo
    fopt = func(xopt)
    return xopt, fopt, iter

def func(x):
    f = x**4-5*x**3-2*x**2+24*x
    return f

def dfunc(x):
    f = 4*x**3-15*x**2-4*x+24
    return f

def ddfunc(x):
    f = 12*x**2-30*x-4
    return f


###############################################
tol = 0.0001
init_guess = 1
[xopt, fopt, iter]=newtonRaphson(init_guess, tol)
print(xopt, fopt, iter)

x = np.linspace(0, 4, 1000)
f = np.linspace(0, 0, len(x))
for i in range(0, len(x), 1):
    f[i] = func(x[i])

p1, = plt.plot(x, f, 'k--', label='f(x)')
p1, = plt.plot(xopt, fopt, 'or',
               label='max[f(x)]', markersize=15, markeredgewidth=3)
plt.show()