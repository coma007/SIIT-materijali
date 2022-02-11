import numpy as np
import matplotlib.pyplot as plt
from nans_lib_2 import rk4N, least_squares_regression, zeroFalsePosition

# a) grafik funkcije 𝑓(𝑥) nad intervalom 𝑥 ∈ [0, 4𝜋] 𝑓(0) = 1 i 𝑓′(0) = 0

# ddfX = lambda x, fX, dfX: -fX + np.cos(3*x) + 1
ddfX = lambda *argv: - argv[1] + np.cos(3*argv[0]) + 1
nfX0 = np.array([1, 0])
a = 0
b = 4*np.pi
h = (b - a)/10000

x = np.arange(a, b+h, h)
fX, _ = rk4N(a, b, h, nfX0, ddfX)
# plt.plot(x, fX)

# b) 𝑓(𝑥) = 1.5 na intervalu 𝑥 ∈ [0, 2𝜋], ako su 𝑓(0) = 0 i 𝑓′(0) = 1
nfX0 = np.array([0, 1])
a = 0
b = 2* np.pi
h = (b - a)/10000

x = np.arange(a, b+h, h)
fX, _ = rk4N(a, b, h, nfX0, ddfX)

p = least_squares_regression(x, fX, 7)
x = np.linspace(a, b, 100)
pX = np.polyval(p, x)
plt.plot(x, pX, 'blue', [a, b], [1.5, 1.5], 'black')

pf = lambda x: np.polyval(p, x) - 1.5
x1, _ = zeroFalsePosition(pf, 0, 2)
print(x1)
plt.scatter(x1, np.polyval(p, x1), c='red')
x2, _ = zeroFalsePosition(pf, 2.5, 5)
print(x2)
plt.scatter(x2, np.polyval(p, x2), c='red')

# c) 𝑓(𝑥) za 𝑥 = 2.6 za uslove pod b)
x26 = 2.6
fX26 = np.polyval(p, x26)
print(fX26)
plt.scatter(x26, fX26, c='orange')
plt.show()
