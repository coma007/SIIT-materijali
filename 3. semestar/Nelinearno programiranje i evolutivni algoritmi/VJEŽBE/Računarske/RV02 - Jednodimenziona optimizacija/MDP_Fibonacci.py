def f(x):
    return -(x**4 - 5*x**3 - 2*x**2 + 24*x)


def fibonacci_method(a, b, tol):

    it = 1
    while (b - a) / tol > fibonacci_number(it):
        it += 1
    print(it)

    x1 = a + fibonacci_number(it-2)/fibonacci_number(it)*(b-a)
    x2 = a + b - x1

    for i in range(2, it+1):
        if f(x1) < f(x2):
            b = x2
            x2 = x1
            x1 = a + b - x2
        else:
            a = x1
            x1 = x2
            x2 = a + b - x1

    if f(x1) < f(x2):
        return x1, f(x1), it
    else:
        return x2, f(x2), it


def fibonacci_number(n):

    if n < 2:
        return 1
    else:
        f1 = 1
        f2 = 1
        for i in range(3, n+1):
            f1, f2 = f2, f1 + f2
        return f2


if __name__ == '__main__':

    optimum, f_optimum, iterations = fibonacci_method(0, 3, 0.0001)
    print(f"x_opt = {optimum}\tf(x_opt) = {f_optimum}\tit = {iterations}")
