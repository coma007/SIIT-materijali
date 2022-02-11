import numpy as np
import matplotlib.pyplot as plt
import eulerN, rk4N, fp2

sT0 = 0
vT0 = 0


ns0T = np.array([sT0, vT0])


t0 = 0
t1 = 60*20
h = (t1 - t0)/10000

sRK4, val = rk4N.rk4N(t0, t1, h, ns0T, fp2.fp2, 0.0) 

x= np.arange(t0, t1, h)
plt.plot(x, sRK4)
plt.show()
sT1 = sRK4[-1]