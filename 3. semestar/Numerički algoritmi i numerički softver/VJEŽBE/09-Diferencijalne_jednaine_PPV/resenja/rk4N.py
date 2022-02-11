import numpy as np
import matplotlib.pyplot as plt

def rk4N(a, b, h, nfX0, dnfX, plotSpeed):
    if plotSpeed <= 0:
        return rk4NWithoutPlot(a, b, h, nfX0, dnfX)
    return rk4NWithPlot(a, b, h, nfX0, dnfX, plotSpeed)

def rk4NWithoutPlot(a, b, h, nfX0, dnfX):
    x = np.arange(a, b, h)
    n = len(x)
    order = len(nfX0)
    fnX = np.empty([order, n])
    fnX[:, 0] = nfX0.T
    k1,k2, k3, k4 = np.empty((1,order)), np.empty((1,order)), np.empty((1,order)), np.empty((1,order))
    for it in range(1, n):
        # k1
        for itOrder in range(order-1):
            k1[0,itOrder] = fnX[itOrder + 1, it - 1]

        args = [x[it-1]]

        for i in range(len(fnX)):
            args.append(fnX[i, it - 1])

        k1[0,order-1] = dnfX(*args)
        
        # k2
        for itOrder in range(order - 1):
            k2[0,itOrder] = fnX[itOrder + 1, it - 1] + h/2*k1[0,itOrder + 1]
       
        args = [x[it-1]+ h/2]
      
        for i in range(len(fnX)):
            for j in range(len(k1)):
                args.append(fnX[i, it - 1]+ h/2*k1[j][0])
           
        k2[0,order-1] = dnfX(*args)

        # k3
        for itOrder in range(order - 1):
            k3[0,itOrder] = fnX[itOrder + 1, it - 1] + h/2*k2[0,itOrder + 1]

        args = [x[it-1]+ h/2]
        for i in range(len(fnX)):
            for j in range(len(k1)):
                args.append(fnX[i, it - 1]+ h/2*k2[j][0])        
        k3[0,order-1] = dnfX(*args)
         
        # k4
        for itOrder in range(order - 1):
            k4[0,itOrder] = fnX[itOrder + 1, it - 1] + h*k3[0,itOrder + 1]

        args = [x[it-1]+ h]
        for i in range(len(fnX)):
            for j in range(len(k1)):
                args.append(fnX[i, it - 1]+  h*k3[j][0])   
     
        k4[0,order-1] = dnfX(*args)

        for itOrder in range(order):
            fnX[itOrder, it] = fnX[itOrder, it - 1] + h/6*(k1[0,itOrder] + 2*k2[0,itOrder] + 2*k3[0,itOrder] + k4[0,itOrder])
       
    
    fX = fnX[0, :]
    return fX, fnX.T

def rk4NWithPlot(a, b, h, nfX0, dnfX, plotSpeed):
    x = np.arange(a, b, h)
    n = len(x)
    order = len(nfX0)
    fnX = np.empty([order, n])
    fnX[:, 0] = nfX0.T
    k1,k2, k3, k4 = np.empty((1,order)), np.empty((1,order)), np.empty((1,order)), np.empty((1,order))
    for it in range(1, n):
        # k1
        for itOrder in range(order-1):
            k1[0,itOrder] = fnX[itOrder + 1, it - 1]

        args = [x[it-1]]

        for i in range(len(fnX)):
            args.append(fnX[i, it - 1])

        k1[0,order-1] = dnfX(*args)
        
        # k2
        for itOrder in range(order - 1):
            k2[0,itOrder] = fnX[itOrder + 1, it - 1] + h/2*k1[0,itOrder + 1]
       
        args = [x[it-1]+ h/2]
      
        for i in range(len(fnX)):
            for j in range(len(k1)):
                args.append(fnX[i, it - 1]+ h/2*k1[j][0])
           
        k2[0,order-1] = dnfX(*args)

        # k3
        for itOrder in range(order - 1):
            k3[0,itOrder] = fnX[itOrder + 1, it - 1] + h/2*k2[0,itOrder + 1]

        args = [x[it-1]+ h/2]
        for i in range(len(fnX)):
            for j in range(len(k1)):
                args.append(fnX[i, it - 1]+ h/2*k2[j][0])        
        k3[0,order-1] = dnfX(*args)
         
        # k4
        for itOrder in range(order - 1):
            k4[0,itOrder] = fnX[itOrder + 1, it - 1] + h*k3[0,itOrder + 1]

        args = [x[it-1]+ h]
        for i in range(len(fnX)):
            for j in range(len(k1)):
                args.append(fnX[i, it - 1]+  h*k3[j][0])   
     
        k4[0,order-1] = dnfX(*args)

        for itOrder in range(order):
            fnX[itOrder, it] = fnX[itOrder, it - 1] + h/6*(k1[0,itOrder] + 2*k2[0,itOrder] + 2*k3[0,itOrder] + k4[0,itOrder])
        plt.plot(x, fnX[0, :], 'blue', [a, b], [0, 0], 'black')
        plt.pause(1/plotSpeed)
    
    fX = fnX[0, :]
    return fX, fnX.T

