import numpy as np
from ddf import ddf
from df import df
from f import f
from finiteDifference import finiteDifference
from matplotlib.pylab import plt
    

left = lambda *args: ddf(args[1]) + 2*df(args[1]) + f(args[1])

right = lambda x: x**2

x1 = 0
fX1 = 0.2
x2 = 1
fX2 = 0.8
h = (x2 - x1)/100

x = np.arange(x1, x2, h)

fX = finiteDifference(left, right, x1, fX1, x2, fX2, h)

plt.plot(x, fX)
plt.show()