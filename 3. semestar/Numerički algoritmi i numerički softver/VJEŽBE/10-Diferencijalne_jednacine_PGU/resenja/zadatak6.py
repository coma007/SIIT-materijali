import numpy as np
from ddf import ddf
from df import df
from f import f
from finiteDifference import finiteDifference
from matplotlib.pylab import plt
from lSquares import lSquares
from zeroFalsePosition import zeroFalsePosition   


left = lambda *args: np.cos(args[0])**2 *ddf(args[1]) - df(args[1])

right = lambda x: 0 

x1 = 0
fX1 = 0
x2 = np.pi
fX2 = 1
h = (x2 - x1)/100

x = np.arange(x1, x2, h)

fX = finiteDifference(left, right, x1, fX1, x2, fX2, h)
p = lSquares(x, fX, 7)
x = np.linspace(x1, x2, 100)
pX = np.polyval(p, x)
plt.plot(x, pX, [0, np.pi], [1,1])
function = lambda x: np.polyval(p, x) - 1.0

x1,a = zeroFalsePosition(function, 0, 1.5, 10^-5,100, 0.0)
x2,a = zeroFalsePosition(function, 1.5, 2, 10^-5, 100,0.0)
x3,a = zeroFalsePosition(function, 2, 2.5, 10^-5,100, 0.0)
x4,a = zeroFalsePosition(function, 2.5, 3, 10^-5,100, 0.0)
print(x1, x2, x3, x4)
plt.scatter([x1, x2, x3, x4], [np.polyval(p, x1), np.polyval(p, x2), np.polyval(p, x3), np.polyval(p, x4)])
plt.show()


