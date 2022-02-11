import numpy as np
import matplotlib.pyplot as plt

def finiteDifference(left, right, x0, fX0, xN, fXN, h):
    x = np.arange(x0, xN+h, h)
    dim = len(x) - 2
    if dim < 3: 
        raise np.ERR_PRINT('Too few intervals!')
    
    A = np.zeros([dim, dim], dtype= np.float64)
    b = np.zeros([dim,1])
    for it in range(dim):
        m = left(x[it + 1], h)
        mid = np.round(len(m)/2) - 1
        fromA = max(0, it - mid)
        toA = min(dim, it + mid + 1)
        fromM = mid - it + fromA
        toM = mid - it + toA

        A[it, int(fromA):int(toA)] = m[int(fromM):int(toM)]
        
        b[it] = right(x[it + 1])
    
    mA = left(x[1], h)
    b[0] =  b[0] - mA[int(mid) - 1]*fX0
   
    mB = left(x[-2], h)
    b[-1]=  b[-1] - mB[int(mid) + 1]*fXN
    
    fX = np.linalg.solve(A,b)
    fxx = [fX0]
    for i in range(len(fX)):
        fxx.append(fX[i][0])
    fxx.append(fXN)

    return fxx

