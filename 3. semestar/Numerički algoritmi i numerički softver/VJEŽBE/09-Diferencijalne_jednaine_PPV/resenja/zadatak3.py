import numpy as np
import matplotlib.pyplot as plt
import eulerN, rk4N
# % f"(x) = -f(x) + x + 2
# % f(0) = 4, f'(0) = 2
# % rešenje: f(x) = 2cos(x) + sin(x) + x + 2

# % eksplicitni oblik jedna?ine po najvisem izvodu funkcije
# % zbog uniformnosti pozivanja moraju kao parametri da se navedu svi redovi
# % izvoda, iako se ne koriste
ddfX = lambda *argv:  - argv[1] + argv[0] + 2
# % PPV mora da ima definisane vrednosti svih izvoda funkcije do reda
# % za 1 manjeg od reda jedna?ine u po?etnoj ta?ki

nfX0 = np.array([4,2])
a = 0
b = 4*np.pi
h = (b - a)/10000


x = np.arange(a, b, h)

f_true = 2*np.cos(x) + np.sin(x) + x + 2
f_x_euler, sss = eulerN.eulerN(a, b, h, nfX0, ddfX, 0.0)
f_x_rk4, sss1 = rk4N.rk4N(a, b, h, nfX0, ddfX, 0.0)

plt.plot(x, f_true, 'red')
plt.plot(x, f_x_euler, 'blue')
plt.plot(x, f_x_rk4, 'red')
plt.show()

