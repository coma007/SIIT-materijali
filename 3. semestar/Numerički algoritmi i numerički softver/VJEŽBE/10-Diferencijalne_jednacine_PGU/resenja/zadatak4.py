import numpy as np
from ddf import ddf
from df import df
from f import f
from finiteDifference import finiteDifference
from matplotlib.pylab import plt
from lSquares import lSquares

left = lambda *args: -2*ddf(args[1]) + df(args[1]) + f(args[1])/2

right = lambda x: np.sin(x)/(x+1)
x1 = 0
fX1 = 0
x2 = 10
fX2 = 3.5
h = (x2 - x1)/100

x = np.arange(x1, x2, h)

fX = finiteDifference(left, right, x1, fX1, x2, fX2, h)

p = lSquares(x, fX, 7)

x = np.linspace(x1, x2, 100)
pX = np.polyval(p, x)
plt.plot(x, pX, 'blue', [x1, x2], [0 ,0 ],'black')

x5 = 5
pX5 = np.polyval(p, x5)
plt.scatter(x5, pX5, c= 'g')
print(pX5)
plt.show()