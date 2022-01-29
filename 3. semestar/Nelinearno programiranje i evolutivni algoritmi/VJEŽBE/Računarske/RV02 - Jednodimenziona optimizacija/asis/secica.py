import numpy as np
import matplotlib.pyplot as plt
import math

def secica(x1, x0, tol):
    x_pre = x0
    x_ppre = math.inf
    x_novo = x1
    iter = 0
    x_niz = [x_pre, x_novo]

    while(abs(x_novo-x_pre) > tol):
        iter += 1
        x_ppre = x_pre
        x_pre = x_novo
        x_novo = x_pre-dfunc(x_pre)*(x_pre-x_ppre)/(dfunc(x_pre)-dfunc(x_ppre))
        x_niz.append(x_novo)
    xopt = x_novo
    fopt = func(xopt)
    return xopt, fopt, iter, x_niz

def func(x):
    f = x**4-5*x**3-2*x**2+24*x
    return f

def dfunc(x):
    f = 4*x**3-15*x**2-4*x+24
    return f

###############################################
tol = 0.0001
init_guess1 = 0
init_guess2 = 3
x = np.linspace(0, 4, 1000)
f = np.linspace(0, 0, len(x))
for i in range(0, len(x), 1):
    f[i] = func(x[i])

p1, = plt.plot(x, f, 'k--', label='f(x)')

[xopt, fopt, iter, x_niz] = secica(init_guess1, init_guess2, tol)
print(xopt, fopt, iter)
for i in range(0, len(x_niz)-1):
    plt.plot([x_niz[i], x_niz[i+1]], [func(x_niz[i] ), func(x_niz[i+1] )] , '-ob',  markersize=5, markeredgewidth=3)
p1, = plt.plot(xopt, fopt, '*r', label='max[f(x)]', markersize=15, markeredgewidth=3)
plt.grid(True)
plt.show()