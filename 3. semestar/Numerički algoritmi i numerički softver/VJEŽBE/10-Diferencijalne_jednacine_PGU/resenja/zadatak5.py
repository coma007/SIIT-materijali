import numpy as np
from ddf import ddf
from df import df
from f import f
from finiteDifference import finiteDifference
from matplotlib.pylab import plt
from lSquares import lSquares


left = lambda *args: -2*ddf(args[1])

right = lambda x: -np.power(x,3) +2 

x1 = 2
fX1 = 2
x2 = 4
fX2 = -2
h = (x2 - x1)/100

x = np.arange(x1, x2, h)

fX = finiteDifference(left, right, x1, fX1, x2, fX2, h)
p = lSquares(x, fX, 7)
x = np.linspace(x1, x2, 100)
pX = np.polyval(p, x)
plt.plot(x, pX)

x3 = 3;
pX3 = np.polyval(p, x3)

plt.scatter(x3, pX3)
plt.show()


