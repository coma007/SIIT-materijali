import numpy as np
from ddf import ddf
from df import df
from f import f
from finiteDifference import finiteDifference
from matplotlib.pylab import plt
from lSquares import lSquares
from zeroFalsePosition import zeroFalsePosition   

left = lambda *args: -4* ddf(args[1]) + df(args[1])/2

right = lambda t: np.sin(t)

t1 = 3
vT1 = 20
t2 = 10
vT2 = 90
h = (t2 - t1)/100

t = np.arange(t1, t2, h)

fT = finiteDifference(left, right, t1, vT1, t2, vT2, h)
p = lSquares(t, fT, 1)
# pretpostavljeni interval
t = np.linspace(0, t2, 100)
pT = np.polyval(p, t)
plt.plot(t, pT, [0, t2], [0,0], 'black')

# a)
tN = 7.5
pTN = np.polyval(p, tN)
plt.scatter(tN, pTN)

# b)
function = lambda x: np.polyval(p, x)
t0, l = zeroFalsePosition(function, 0, 2.5, 10^-5,100, 0.0)
print(t0)
pT0 = np.polyval(p, t0)
plt.scatter(t0, pT0)

plt.show()


