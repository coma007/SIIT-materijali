import numpy as np
import matplotlib.pyplot as plt
from nans_lib_2 import f, df, ddf, finiteDifference, least_squares_regression, zeroFalsePosition

# (sin 2𝑥)^3𝑓′′(𝑥) + 𝑓′(𝑥) + 2𝑥^2 = 3

# a) grafik funkcije 𝑓(𝑥) za 𝑓(1) = 0 i 𝑓(4) =𝜋/2
left = lambda x, fX: np.sin(2*x)**3 * ddf(fX) + df(fX)
right = lambda x: 3 - 2 * x ** 2
# left = lambda *argv: np.sin(2*argv[0])**3 * ddf(argv[1]) + df(argv[1])
# right = lambda *argv: 3 - 2 * argv[0] ** 2

x1 = 1
fX1 = 0
x2 = 4
fX2 = np.pi/2
h = (x2 - x1) / 100

x = np.arange(x1, x2 + h, h)
fX = finiteDifference(left, right, x1, fX1, x2, fX2, h)
# plt.plot(x, fX)

# b) 𝑓(𝑥) = 13, ako važi 𝑓(𝜋4) = 0 i 𝑓(𝜋) = 1
x1 = np.pi/4
fX1 = 0
x2 = np.pi
fX2 = 1
h = (x2 - x1) / 100

x = np.arange(x1, x2 + h, h)
fX = finiteDifference(left, right, x1, fX1, x2, fX2, h)
# plt.plot(x, fX, 'cyan')

p = least_squares_regression(x, fX, 7)
x = np.linspace(x1, x2, 100)
pX = np.polyval(p, x)
plt.plot(x, pX, 'blue', [x1, x2], [13, 13], 'black')

pf = lambda x: np.polyval(p, x) - 13
x1, _ = zeroFalsePosition(pf, 1, 1.5)
print(x1)
plt.scatter(x1, np.polyval(p, x1), c='red')
x2, _ = zeroFalsePosition(pf, 2.5, np.pi)
print(x2)
plt.scatter(x2, np.polyval(p, x2), c='red')

# c) 𝑓(2.3) za uslove pod b)
x23 = 2.3
fX23 = np.polyval(p, x23)
print(fX23)
plt.scatter(x23, fX23, c='orange')

plt.show()
