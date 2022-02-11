import numpy as np
import matplotlib.pyplot as plt
import eulerN, rk4N, zeroFalsePosition, lSquares

dhT = lambda *argv: - np.sin(2*argv[0]) + 0.2*argv[1]

# a)

hT0 =  np.array([2])

t0 = 5.5
tb = 10
step = (tb - t0)/1000

vRK4 = rk4N.rk4N(t0, tb, step, hT0, dhT, 0.0)
r = 3
value = r**2

v1 = np.dot(value*np.pi,hT0)

v2 = np.dot(value*np.pi,vRK4[-1]) 
# zapremina ulivene vode je jednaka razlici zapremina u krajevima intervala
dv = v2 - v1 
#print(dv)



# b)
hT0 = np.array([8])

t0 = 2
# pretpostavljeni dovoljno dug interval
tb = 10 
step = (tb - t0)/1000

hTRK4,  hnTRK4 = rk4N.rk4N(t0, tb, step, hT0, dhT, 0.0)

#aproksimacija funkcije radi nalaženja ta?ke za datu vrednost
#proizvoljan dovoljno dobar stepen polinoma
x =  np.arange(t0, tb, step)

p = lSquares.lSquares(x, hTRK4, 7)

a = 2
b = 10

x = np.linspace(a, b, 100)
hT1 = 16

plt.plot(x, np.polyval(p, x), [a, b], [hT1, hT1])
function =  lambda x: np.polyval(p, x) - hT1
t1,it = zeroFalsePosition.zeroFalsePosition(function, a, b, 10^-5,100, 0.0)
print(t1)
plt.scatter(t1, hT1)

plt.show()









