import numpy as np
import matplotlib.pyplot as plt




def fibonaci_metod(a,b,tol):
    #Fibonacci - jev postupak minimizacije funckcije jedne promenljive.
    # Funkcija mora biti unimodalna nad intervalom [a, b].
    # Tol je trazena sirina intervala u kome se nalazi minimum.
    ## Korak 1 - Trazimo najmanji broj n koji zadovoljava uslov
    n = 1
    while ((b-a)/tol) > fibonaci_broj(n):
        n += 1

    ## Korak 2 - Odredjujemo pocetne tacke

    x1 = a + fibonaci_broj(n-2)/fibonaci_broj(n)*(b-a)
    x2 = a + b - x1

    ## Korak 3 - Iteracije
    # Radimo n - 1 iteracija, posle cega je (b - a) < tol

    for i in range(2, n+1):

        if func(x1) <= func(x2):
            b = x2
            x2 = x1
            x1 = a + b - x2
        else:
            a = x1
            x1 = x2
            x2 = a + b - x1



    if func(x1) < func(x2):
        xopt = x1
        fopt = func(x1)
    else:
        xopt = x2
        fopt = func(x2)

    return xopt, fopt, n


def fibonaci_broj(n):
    if n == 1 or n == 2:
        f = 1
    else:
        fp = 1
        fpp = 1
        for i in range(3, n+1):
            f = fp + fpp
            fpp = fp
            fp = f
    return f


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
xopt, fopt, n = fibonaci_metod(a, b, tol)
print(xopt, fopt, n)
print(fibonaci_broj(n))
