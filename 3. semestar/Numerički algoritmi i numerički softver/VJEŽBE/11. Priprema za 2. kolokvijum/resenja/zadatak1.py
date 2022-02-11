import numpy as np
from nans_lib_2 import integrate_simpson

f = lambda x: 2 * x**2 + 2
g = lambda x: 20 * np.cos(x)

# a) površina između krivih 𝑓(𝑥) i 𝑔(𝑥) nad intervalom 𝑥 ∈ [0, 2.5]
a = 0
b = 2.5

fg = lambda x: np.abs(f(x) - g(x))

P = integrate_simpson(fg, a, b, 100)

# b) zapremina tela dobijenog rotacijom površine ograničene funkcijom 𝑓(𝑥) i x-ose nad intervalom 𝑥 ∈ [0, 2] oko y – ose.

# y = 2x^2 + 2 => x = sqrt((y - 2)/2)
# [0, 2] => [2*0^2 + 2, 2*2^2 + 2] => [2, 10]
a = 0
b = 2

fy = lambda y: np.sqrt((y - 2) / 2)
y1 = 2 * a**2 + 2
y2 = 2 * b**2 + 2

fy_sqr = lambda y: fy(y) ** 2

V1 = np.pi * integrate_simpson(fy_sqr, y1, y2, 100)

# V2 = r2^2*pi*H2 (zapremina cilindra)
V2 = (b - a) ** 2 * np.pi * (y2 - 0)
V = V2 - V1

print(P)
print(V)
