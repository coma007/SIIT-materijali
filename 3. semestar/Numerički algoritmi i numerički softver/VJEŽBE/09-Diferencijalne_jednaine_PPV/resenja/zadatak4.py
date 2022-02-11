import numpy as np
import matplotlib.pyplot as plt
import eulerN, rk4N
# % f(x)"" = -13f"(x) - 36f(x)
# % f(0) = 0, f'(0) = -3, f"(0) = 5, f"'(0) = -3
# % rešenje: f(x) = cos(2x) - 3sin(2x) - cos(3x) + sin(3x)

# % eksplicitni oblik jedna?ine po najvisem izvodu funkcije
# % zbog uniformnosti pozivanja moraju kao parametri da se navedu svi redovi
# % izvoda, iako se ne koriste
ddddfX = lambda *argv: -13*argv[3]- 36*argv[1]

# % PPV mora da ima definisane vrednosti svih izvoda funkcije do reda
# % za 1 manjeg od reda jedna?ine u po?etnoj ta?ki

nfX0 = np.array([0, -3, 5, -3])
a = 0
b = 4*np.pi
h = (b - a)/10000


x = np.arange(a, b, h)

f_true = np.cos(2*x) - 3*np.sin(2*x) - np.cos(3*x) + np.sin(3*x)
f_x_euler, sss = eulerN.eulerN(a, b, h, nfX0, ddddfX, 0.0)
f_x_rk4, sss1 = rk4N.rk4N(a, b, h, nfX0, ddddfX, 0.0)

plt.plot(x, f_true, 'red')
plt.plot(x, f_x_euler, 'blue')
plt.plot(x, f_x_rk4, 'red')
plt.show()


