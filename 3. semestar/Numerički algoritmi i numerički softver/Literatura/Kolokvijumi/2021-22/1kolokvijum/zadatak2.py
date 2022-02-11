import numpy as np
import matplotlib.pyplot as plt
from NANS_lib import *
import sympy as sym

if __name__ == '__main__':

    print("Zadatak 2:\n")

    f = lambda x: np.sin(x**2 - 2)
    g = lambda x: x * np.cos(x)
    a = -3
    b = 1

    ''' a - Nacrtati obje funkcije '''
    x = np.linspace(a, b, 100)
    fX = f(x)
    gX = g(x)
    plt.plot(x, fX, color="blue")
    plt.plot(x, gX, color="red")

    ''' b - Proizvoljnom zatvorenom metodom pronaci i nacrtati nule f '''
    plt.axhline(y=0, color="lightgrey")  # iscrtavanje y = 0
    # postoje tri nule
    zerof1, _ = zeroFalsePosition(f, -3, -2.5)
    zerof2, _ = zeroFalsePosition(f, -2.5, -2)
    zerof3, _ = zeroFalsePosition(f, -1.5, -1)
    plt.scatter(zerof1, f(zerof1), color="black")
    plt.scatter(zerof2, f(zerof2), color="black")
    plt.scatter(zerof3, f(zerof3), color="black")
    print("Presjeci f sa x-osom: ")
    print(f"x1 = {np.round(zerof1, 4)}\tf(x1) = {np.round(f(zerof1), 4)}")
    print(f"x2 = {np.round(zerof2, 4)}\tf(x2) = {np.round(f(zerof2), 4)}")
    print(f"x3 = {np.round(zerof3, 4)}\tf(x2) = {np.round(f(zerof3), 4)}")

    ''' c - Proizvoljnom zatvorenom metodom pronaci i nacrtati sve presjeke f i g '''
    h = lambda x: f(x) - g(x)
    # postoje dva presjeka
    interfg1, _ = zeroSecant(h, -2.5, -2.0)
    interfg2, _ = zeroSecant(h, -1.5, -1.0)
    plt.scatter(interfg1, f(interfg1), color="green")
    plt.scatter(interfg2, f(interfg2), color="green")
    print("\nPresjeci f sa g: ")
    print(f"x1 = {np.round(interfg1, 4)}\t\tf(x1) = {np.round(f(interfg1), 4)}\tg(x1) = {np.round(g(interfg1), 4)}")
    print(f"x2 = {np.round(interfg2, 4)}\tf(x2) = {np.round(f(interfg2), 4)}\tg(x2) = {np.round(g(interfg2), 4)}")

    ''' d - Maksimum f i minimum g '''
    # pronalazenje prvog izvoda f
    x_sym = sym.Symbol("x")
    f_diff = sym.diff(sym.sin(x_sym**2 - 2), x_sym)
    f_diff = sym.lambdify(x_sym, f_diff, 'numpy')
    # ekstrem f je u nuli prvog izvoda
    x_max, _ = zeroFalsePosition(f_diff, -2.5, -1.5)
    plt.scatter(x_max, f(x_max), color="darkblue")
    print("\nMaksimum funkcije f: ")
    print(f"x_max = {np.round(x_max, 4)}\tf(x_max) = {np.round(f(x_max), 4)}")
    # pronalazenje prvog izvoda g
    g_diff = sym.diff(x_sym * sym.cos(x_sym), x_sym)
    g_diff = sym.lambdify(x_sym, g_diff, 'numpy')
    # ekstrem g je u nuli prvog izvoda
    x_min, _ = zeroFalsePosition(g_diff, -1.5, -0.5)
    plt.scatter(x_min, g(x_min), color="darkblue")
    print("Minimum funkcije g: ")
    print(f"x_min = {np.round(x_min, 4)}\tg(x_min) = {np.round(g(x_min), 4)}")

    ''' e - Presjecne tacke f i g sa x = pi/6 '''
    plt.axvline(x=np.pi/6, color="yellow")  # iscratavanje konstantne funkcije x = pi/6
    # postoji jedan presjek f sa pi/6
    plt.scatter(np.pi/6, f(np.pi/6), color="brown")
    print("\nPresjek f sa x = pi/6: ")
    print(f"x1 = {np.round(np.pi/6, 4)}\tf(x1) = {np.round(f(np.pi/6), 4)}")
    # postoji jedan presjek g sa pi/6
    plt.scatter(np.pi/6, g(np.pi/6), color="brown")
    print("Presjek g sa x = pi/6: ")
    print(f"x1 = {np.round(np.pi/6, 4)}\tg(x1) = {np.round(g(np.pi/6), 4)}")

    plt.show()
