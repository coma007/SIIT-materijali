import numpy as np
import matplotlib.pyplot as plt
import math

def zlatni_presek_metod(a, b, tol):
    # Zlatni presek postupak minimizacije funckcije jedne promenljive.
    # Tol je trazena sirina intervala u kome se nalazi minimum.
    ## Korak 1 - Odredjujemo početnu tačku
    # Odredjivanje konstante zlatnog preseka
    c = (3-math.sqrt(5))/2
    # Pocetne tacke
    x1 = a + c*(b-a)
    x2 = a + b-x1
    n = 1
    ## Korak 2 - Iterativno smanjujemo interval dok ne zadovoljimo zadatu preciznost
    while (b-a) > tol:
        n += 1
        if func(x1) <= func(x2):
            b = x2
            x1 = a + c*(b-a)
            x2 = a+b-x1
        else:
            a = x1
            x1 = a + c * (b - a)
            x2 = a + b - x1

    if func(x1) < func(x2):
        xopt = x1
        fopt = func(x1)
    else:
        xopt = x2
        fopt = func(x2)

    return xopt, fopt, n

def func(x):
    f=-1*(x**4-5*x**3-2*x**2+24*x)
    return f

a = 0
b = 3
tol = 0.0001
x = np.linspace(0, 4, 1000)
f = np.linspace(0, 0, len(x))
for i in range(0, len(x), 1):
    f[i] = func(x[i])

p1, = plt.plot(x, f, 'k--', label='f(x)')
plt.show()
xopt, fopt, n=zlatni_presek_metod(a, b, tol)
print(xopt, fopt, n)