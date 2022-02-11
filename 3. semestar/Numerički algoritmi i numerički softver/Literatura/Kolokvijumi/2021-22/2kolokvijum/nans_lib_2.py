import numpy as np

def gauss(A, b):
    '''
    Solves the system of linear equations given by Ax = b using gaussian elimination.

            Parameters:
                    A(np.array, 1d): Coefficient matrix
                    b(np.array, 1d): Constant terms

            Returns:
                    x(np.array, 1d): Solution of the system
    '''

    (n, m) = A.shape
    Aaug = np.zeros((n, n+1))
    Aaug[0:n, 0:n] = A
    Aaug[:, n] = b

    for k in range(n-1):
        for i in range(k+1, n):
            m = -Aaug[i, k]/Aaug[k, k]
            Aaug[i, :] = Aaug[i, :]+m*Aaug[k, :]

    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (Aaug[i, n]-np.dot(Aaug[i, 0:n], x))/Aaug[i, i]
    return x

def gauss_seidel(A, b, x0, errMax=0.0001, itMax=100):
    '''
    Solves the system of linear equations given by Ax = b using the Gauss-Seidel method.

            Parameters:
                    A(np.array, 1d): Coefficient matrix
                    b(np.array, 1d): Constant terms
                    x0(np.array, 1d): Starting point
                    errMax(float): Maximum allowed error
                    itMax(int): Maximum number of iterations

            Returns:
                    x(np.array, 1d): Solution of the system
    '''
    n, _ = A.shape
    x1 = np.zeros(n)
    for _ in range(itMax):
        for i in range(n):
            s = 0
            for j in range(i):
                s = s + A[i, j] * x1[j]
            for j in range(i + 1,n):
                s = s + A[i, j] * x0[j]
            x1[i] = (b[i] - s)/A[i, i]
        if np.linalg.norm(x0 - x1, np.Inf) < errMax:
            break
        x0 = x1.copy()
    return x1

def jacobi(A, b, x0, errMax=0.0001, itMax=100):
    '''
    Solves the system of linear equations given by Ax = b using the jacobi method.

            Parameters:
                    A(np.array, 1d): Coefficient matrix
                    b(np.array, 1d): Constant terms
                    x0(np.array, 1d): Starting point
                    errMax(float): Maximum allowed error
                    itMax(int): Maximum number of iterations

            Returns:
                    x(np.array, 1d): Solution of the system
    '''
    n, _ = A.shape
    x1 = np.zeros(n)
    for _ in range(itMax):
        for i in range(n):
            s = 0
            for j in range(n):
                if i != j:
                    s = s + A[i, j] * x0[j]
                x1[i] = (b[i] - s)/A[i, i]
        if np.linalg.norm(x0 - x1, np.Inf) < errMax:
            break
        x0 = x1.copy()
    return x1

def zeroBisection(f, a, b, errMax=0.0001, itMax=100):
    '''
    Finds the zero of a function using the Bisection method

            Parameters:
                    f(function): Target function
                    a(np.array, 1d): Left boundry
                    b(np.array, 1d): Right boundry
                    errMax(float): Maximum allowed error
                    itMax(int): Maximum number of iterations

            Returns:
                    x(np.array, 1d): x where f(x)==0
                    it: number of performed iterations
    '''
    for it in range(itMax):
        zero = (a + b)/2
        fZero = f(zero)

        if abs(fZero) < errMax or abs(b - a) < errMax:
            return zero, it + 1
        
        if f(a)*fZero < 0:
            b = zero
        else:
            a = zero

    return zero, it + 1

def zeroFalsePosition(f, a, b, errMax=0.0001, itMax=100):
    '''
    Finds the zero of a function using the FalsePosition method

            Parameters:
                    f(function): Target function
                    a(np.array, 1d): Left boundry
                    b(np.array, 1d): Right boundry
                    errMax(float): Maximum allowed error
                    itMax(int): Maximum number of iterations

            Returns:
                    x(np.array, 1d): x where f(x)==0
                    it: number of performed iterations
    '''
    for it in range(itMax):
        fA = f(a)
        fB = f(b)
        zero = b - fB*(b - a)/(fB - fA)

        fZero = f(zero)

        if abs(fZero) < errMax or abs(b - a) < errMax:
            return zero, it

        if fA*fZero < 0:
            b = zero
        else:
            a = zero

    return zero, it

def zeroNewton(f, df, x0, errMax=0.0001, itMax=100):
    '''
    Finds the zero of a function using the Newton method

            Parameters:
                    f(function): Target function
                    df(function): Derivative function
                    x0(np.array, 1d): Starting point
                    errMax(float): Maximum allowed error
                    itMax(int): Maximum number of iterations

            Returns:
                    x(np.array, 1d): x where f(x)==0
                    it: Number of performed iterations
    '''

    for it in range(itMax):
        zero = x0 - f(x0)/df(x0)

        fZero = f(zero)
        if abs(fZero) < errMax:
            return zero, it + 1
        
        x0 = zero

    return zero, it + 1

def zeroSecant(f, a, b, errMax=0.0001, itMax=100):
    '''
    Finds the zero of a function using the Secant method

            Parameters:
                    f(function): Target function
                    a(np.array, 1d): Left boundry
                    b(np.array, 1d): Right boundry
                    errMax(float): Maximum allowed error
                    itMax(int): Maximum number of iterations

            Returns:
                    x(np.array, 1d): x where f(x)==0
                    it: number of performed iterations
    '''
    for i in range(itMax):
        fA = f(a)
        fB = f(b)
        zero = b - fB*(b - a)/(fB - fA)

        fZero = f(zero)

        if abs(fZero) < errMax:
            return zero, i + 1
        
        a = b
        b = zero

    return zero, i + 1


def lagrange_interpolation(x, fX):
    '''
    Finds the Lagrange polynomial for given points

            Parameters:
                    x(np.array, 1d): Points on x axis
                    fX(np.array, 1d): Points on y axis

            Returns:
                    p(np.array, 1d): Lagrange polynomial coefficients such that 
                                     L = p[0]*x**(N-1) + p[1]*x**(N-2) + ... + p[N-2]*x + p[N-1]
    '''
    order = x.size

    p = 0

    for itFX in range(order):
        lNumer = 1
        lDenom = 1

        for itX in range(itFX):
            lNumer = np.convolve(lNumer, np.array([1, -x[itX]]))
            lDenom = lDenom * (x[itFX] - x[itX])
        
        for itX in range(itFX+1, order):
            lNumer = np.convolve(lNumer, np.array([1, -x[itX]]))
            lDenom = lDenom*(x[itFX] - x[itX])

        p = p + lNumer/lDenom*fX[itFX]

    return p


def least_squares_regression(x, fX, order):
    '''
    Performs least-squares regression with polynomial of given order

            Parameters:
                    x(np.array, 1d): Points on x axis
                    fX(np.array, 1d): Points on y axis
                    order(int): Polynomial order

            Returns:
                    p(np.array, 1d): Polynomial coefficients of the least-squares solution such that 
                                     R = p[0]*x**(N-1) + p[1]*x**(N-2) + ... + p[N-2]*x + p[N-1]
    '''
    n = x.size
    m = min(order+1, n)
    A = np.zeros((n, m))

    for it in range(m):
        A[:, it] = x**(it)
    
    a = np.linalg.solve(np.matmul(A.T, A), np.matmul(A.T, fX))

    p = a[::-1]
    return p


def integrate_simpson(f, a, b, intervals):
    '''
    Performs integration of given funtion for givne interval with Simpson method

            Parameters:
                    f(callable): Function to integrate
                    a(int): Start of interval
                    b(int): End of interval
                    intervals(int): Number of subintervals

            Returns:
                    I(int): Calculated integral value
    '''
    x = np.linspace(a, b, intervals + 1)
    fX = f(x)
    width = (b-a)/intervals

    I = 0
    for it in range(0, intervals, 2):
        fX1 = fX[it]
        fX2 = fX[it + 1]
        fX3 = fX[it + 2]

        I = I + (fX1 + 4*fX2 + fX3) * width/3
    return I


def rk4N(a, b, h, nfX0, dnfX):
    '''
    Solves differential given with initial value problem using Runge-Kutta 4 method

            Parameters:
                    a(int): Start of interval
                    b(int): End of interval
                    h(int): Interval step
                    nfX0(np.array, 1d): Initial values
                    dnfX(callable): Differential equation

            Returns:
                    fX(np.array, 1d): Values of f function
                    fnX(np.array, 2d): Values of every needed f derivative and f function
    '''
    x = np.arange(a, b+h, h)
    n = len(x)
    order = len(nfX0)
    fnX = np.empty([order, n])
    fnX[:, 0] = nfX0.T
    k1, k2, k3, k4 = np.empty((1,order)), np.empty((1,order)), np.empty((1,order)), np.empty((1,order))
    for it in range(1, n):
        for itOrder in range(order-1):
            k1[0,itOrder] = fnX[itOrder + 1, it - 1]

        args = [x[it-1]]

        for i in range(len(fnX)):
            args.append(fnX[i, it - 1])

        k1[0,order-1] = dnfX(*args)
        
        for itOrder in range(order - 1):
            k2[0,itOrder] = fnX[itOrder + 1, it - 1] + h/2*k1[0,itOrder + 1]
       
        args = [x[it-1]+ h/2]
      
        for i in range(len(fnX)):
            for j in range(len(k1)):
                args.append(fnX[i, it - 1]+ h/2*k1[j][0])
           
        k2[0,order-1] = dnfX(*args)

        for itOrder in range(order - 1):
            k3[0,itOrder] = fnX[itOrder + 1, it - 1] + h/2*k2[0,itOrder + 1]

        args = [x[it-1]+ h/2]
        for i in range(len(fnX)):
            for j in range(len(k1)):
                args.append(fnX[i, it - 1]+ h/2*k2[j][0])        
        k3[0,order-1] = dnfX(*args)
         
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
    return fX, fnX


def f(h):
    '''
    Performs finite difference vector transformation for function f

            Parameters:
                    h(int): Point on x-axis

            Returns:
                    fX(int): Transformed value
    '''
    arr = np.array([0, 1, 0])
    fX = arr
    return fX


def df(h):
    '''
    Performs finite difference vector transformation for first derivative of function f

            Parameters:
                    h(int): Point on x-axis

            Returns:
                    fX(int): Transformed value
    '''
    arr = np.array([0, -1, 1])
    fX = arr/h
    return fX


def ddf(h):
    '''
    Performs finite difference vector transformation for second derivative of function f

            Parameters:
                    h(int): Point on x-axis

            Returns:
                    fX(int): Transformed value
    '''
    arr = np.array([1, -2, 1])
    fX = arr/(h**2)
    return fX


def finiteDifference(left, right, x0, fX0, xN, fXN, h):
    '''
    Solves differential equation given with boundary value problem using finite difference method

            Parameters:
                    left(callable): Left side of the differential equation
                    right(callable): Right side of the differential equation
                    x0(int): X-axis value of left boundary
                    fX0(int): Y-axis value of left boundary
                    xN(int): X-axis value of right boundary
                    fXN(int): Y-axis value of right boundary
                    h(int): Interval step

            Returns:
                    fxx(np.array, 1d): Values of f function
    '''
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
