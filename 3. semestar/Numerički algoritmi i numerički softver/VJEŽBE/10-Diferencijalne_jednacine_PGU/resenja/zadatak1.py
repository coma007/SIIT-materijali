import numpy as np
import matplotlib.pylab as plt
from finiteDifference import finiteDifference
from ddf import ddf


#  f(x)" = -sin(x)
#  f(0) = 0
#  f(2*pi) = 0
#  resenje: f(x) = sin(x)

#  u levoj strani jednacine figurisu funkcija, njeni izvodi i njihovi
#  množioci
#  u desnoj strani jednacine figurise samo nezavisno promenljiva i slobodne
#  konstante
left = lambda *args: ddf(args[1])
right = lambda x: -np.sin(x)

#PGU ima definisanu vrednost funkcije u granicama intervala

x1 = 0
fX1 = 0
x2 = 2*np.pi 
fX2 = 0
h = (x2 - x1)/100

x = np.arange(x1, x2, h)
fX = finiteDifference(left, right, x1, fX1, x2, fX2, h)
plt.plot(x, fX)
plt.show()