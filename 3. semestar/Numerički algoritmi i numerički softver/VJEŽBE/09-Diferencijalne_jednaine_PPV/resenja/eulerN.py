import numpy as np
import matplotlib.pyplot as plt

def eulerN(a, b, h, nfX0, dnfX, plot_speed):
    if plot_speed <= 0:
        return eulerNWithoutPlot(a, b, h, nfX0, dnfX)
    return eulerNWithPlot(a, b, h, nfX0, dnfX, plot_speed)


def eulerNWithoutPlot(a, b, h, nfX0, dnfX):
    x = np.arange(a, b, h)
    n = len(x)
    # red diferencijalne jednacine
    order = len(nfX0)
    # matrica praznih vrednosti fX funkcije i njenih izvoda
    fnX = np.empty([order, n], dtype='object')
    # dodelimo prvom elementu vektora vrednosti pocetnu vrednost uslova
    # vrednosti se dodeljuju prvoj koloni tj. dodela po nultoj koloni
    fnX[:,0] = nfX0.T
    

    # krecemo od drugog clana jer smo u prethodnom koraku dodelili vrednost prvom clanu
    for it in range(1, n):
        # f(i) = f(i - 1) + h*f'(i - 1);
        # f'(i) = f'(i - 1) + h*f"(i - 1);
        # .
        # .
        # .
        for itOrder in range(order-1):
            fnX[itOrder, it] = fnX[itOrder, it - 1] + h*fnX[itOrder + 1, it - 1]
        
        # lista argumenata: [x(1) f(1) f'(1) ... f^(r-1)(1)]
        args = [x[it-1]]
        for i in range(len(fnX)):
            args.append(fnX[i, it - 1])
        
        fnX[order-1, it] = fnX[order-1, it - 1] + h*dnfX(*args)
    # prva vrsta cuva vrednosti funkcije
    fX = fnX[0, :]
 
    return fX, fnX.T

def eulerNWithPlot(a, b, h, nfX0, dnfX, plotSpeed):
    x = np.arange(a, b, h)
    n = len(x)
    # red diferencijalne jednacine
    order = len(nfX0)
    # matrica praznih vrednosti fX funkcije i njenih izvoda
    fnX = np.empty([order, n])
    # dodelimo prvom elementu vektora vrednosti pocetnu vrednost uslova
    # vrednosti se dodeljuju prvoj koloni tj. dodela po nultoj koloni
    fnX[:,0] = nfX0.T
    

    # krecemo od drugog clana jer smo u prethodnom koraku dodelili vrednost prvom clanu
    for it in range(1, n):
        # f(i) = f(i - 1) + h*f'(i - 1);
        # f'(i) = f'(i - 1) + h*f"(i - 1);
        # .
        # .
        # .
        for itOrder in range(order-1):
            fnX[itOrder, it] = fnX[itOrder, it - 1] + h*fnX[itOrder + 1, it - 1]
        
        # lista argumenata: [x(1) f(1) f'(1) ... f^(r-1)(1)]
        args = [x[it-1]]
        for i in range(len(fnX)):
            args.append(fnX[i, it - 1])
        
        fnX[order-1, it] = fnX[order-1, it - 1] + h*dnfX(*args)
        plt.plot(x, fnX[0, :], 'blue', [a, b], [0 ,0], 'black')
        plt.pause(1/plotSpeed)
    # prva vrsta cuva vrednosti funkcije
    fX = fnX[0, :]
 
    return fX, fnX.T