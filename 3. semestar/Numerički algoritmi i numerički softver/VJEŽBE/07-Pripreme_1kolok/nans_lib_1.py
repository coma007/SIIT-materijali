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
