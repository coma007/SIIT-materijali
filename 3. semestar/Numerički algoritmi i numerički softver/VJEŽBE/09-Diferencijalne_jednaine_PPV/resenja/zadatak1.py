import numpy as np
import matplotlib.pyplot as plt
import eulerN, rk4N
# % f(x)' = cos(x)
# % f(0) = 0
# % rešenje: f(x) = sin(x)

# % eksplicitni oblik jedna?ine po najvišem izvodu funkcije
# % zbog uniformnosti pozivanja moraju kao parametri da se navedu svi redovi
# % izvoda, iako se ne koriste

dnfX = lambda *argv: np.cos(argv[0])

# PPV mora da ima definisanu vrednost funkcije u po?etnoj ta?ki
nfX0 = np.array([0])
a = 0
b = 2*np.pi
h = (b - a)/10000;

x = np.arange(a, b, h)

f_true = np.sin(x)

#f_x_euler,sss = eulerN.eulerN(a, b, h, nfX0, dnfX, 0.0)
f_x_rk4, sss1 = rk4N.rk4N(a, b, h, nfX0, dnfX, 0.0)

plt.plot(x, f_true, 'black')
#plt.plot(x, f_x_euler, 'red')
#plt.plot(x, f_x_rk4, 'blue')
plt.show()