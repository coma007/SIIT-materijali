import numpy as np
import matplotlib.pyplot as plt
import eulerN, rk4N
# % f"(x) = -sin(x)
# % f(0) = 0, f'(0) = 1
# % rešenje: f(x) = sin(x)

# % eksplicitni oblik jedna?ine po najvišem izvodu funkcije
# % zbog uniformnosti pozivanja moraju kao parametri da se navedu svi redovi
# % izvoda, iako se ne koriste

ddfX = lambda *argv: - np.sin(argv[0])

# % PPV mora da ima definisane vrednosti svih izvoda funkcije do reda
# % za 1 manjeg od reda jedna?ine u po?etnoj ta?ki

nfX0 = np.array([0,1])
a = 0
b = 4*np.pi
h = (b - a)/10000

x = np.arange(a, b, h)

f_true = np.sin(x)
f_x_euler, sss = eulerN.eulerN(a, b, h, nfX0, ddfX, 0.0)
f_x_rk4, sss1 = rk4N.rk4N(a, b, h, nfX0, ddfX, 0.0)

plt.plot(x, f_true, 'red')
plt.plot(x, f_x_euler, 'blue')
plt.plot(x, f_x_rk4, 'red')
plt.show()