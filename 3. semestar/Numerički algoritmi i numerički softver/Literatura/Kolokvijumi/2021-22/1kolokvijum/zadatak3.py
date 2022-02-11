import matplotlib.pyplot as plt
from NANS_lib import *

if __name__ == '__main__':

    print("Zadatak 3:\n")

    f = lambda x: np.sqrt(2) * np.sin(2*x) + np.cos(-x/3)
    a = - np.pi/2
    b = 4*np.pi/3

    x = np.linspace(a, b, 100)
    fX = f(x)

    ''' a - Crtanje funkcije '''
    plt.plot(x, fX, color="blue")

    ''' b - Priprema tacaka za interpolaciju '''
    # potreban broj tacaka za interpolaciju 4. stepenom je 5
    x_approx4 = np.linspace(a, b, 5)
    fX_approx4 = f(x_approx4)
    plt.scatter(x_approx4, fX_approx4, color="green")

    ''' c - Aproksimacija funkcije polinomom 4. stepena '''
    p4 = lagrange_interpolation(x_approx4, fX_approx4)
    print("Aproksimacija polinomom 4. stepena: p = ", np.round(p4, 4))
    pX = np.polyval(p4, x)
    plt.plot(x, pX, color="red")

    ''' d - Aproksimacija funkcije polinomom 3. stepena '''
    x_approx3 = np.linspace(a, b, 100)
    fX_approx3 = f(x_approx3)
    p3 = least_squares_regression(x_approx3, fX_approx3, 3)
    print("Aproksimacija polinomom 3. stepena: p = ", np.round(p3, 4))
    pX = np.polyval(p3, x)
    plt.plot(x, pX, color="brown")

    ''' e - Presjek polinoma stepena 3 i 4 '''
    g = lambda x: np.polyval(p4, x) - np.polyval(p3, x)
    x1_g, _ = zeroFalsePosition(g, a, -1)
    x2_g, _ = zeroFalsePosition(g, 0, 1)
    x3_g, _ = zeroFalsePosition(g, 2, 3)
    plt.scatter(x1_g, np.polyval(p4, x1_g), color="orange")
    plt.scatter(x2_g, np.polyval(p4, x2_g), color="orange")
    plt.scatter(x3_g, np.polyval(p4, x3_g), color="orange")
    print("\nPresjeci polinoma 3. i 4. stepena:")
    print(f"x1 = {np.round(x1_g, 4)}\nx2 = {np.round(x2_g, 4)}\nx3 = {np.round(x3_g, 4)}")

    plt.show()
