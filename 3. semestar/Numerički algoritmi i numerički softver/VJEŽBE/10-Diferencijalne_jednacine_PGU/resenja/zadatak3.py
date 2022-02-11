import numpy as np
from ddf import ddf
from df import df
from f import f
from finiteDifference import finiteDifference
from matplotlib.pylab import plt

left = lambda *args: 2*np.square(args[0])*ddf(args[1]) - 4*df(args[1]) + np.sin(args[0])*f(args[1])

right = lambda x: np.sqrt(x)

x1 = 0
fX1 = 0
x2 = 2
fX2 = 1
h = (x2 - x1)/100

x = np.arange(x1, x2, h)

fX = finiteDifference(left, right, x1, fX1, x2, fX2, h)

plt.plot(x, fX)
plt.show()