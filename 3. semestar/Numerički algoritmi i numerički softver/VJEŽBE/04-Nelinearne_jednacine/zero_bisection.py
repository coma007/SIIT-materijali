import numpy as np
from matplotlib import pyplot as plt

def zero_bisection(f, a, b, err_max=0.001, it_max=100, plot_speed=-1):
    if f(a)*f(b) > 0:
        raise Exception('Invalid parameters: f(a)*f(b) > 0!')

    if plot_speed <= 0:
        return zero_bisection_no_plot(f, a, b, err_max, it_max)

    return zero_bisection_plot(f, a, b, err_max, it_max, plot_speed)


def zero_bisection_no_plot(f, a, b, err_max, it_max):
    for it in range(it_max):
        zero = (a + b)/2
        f_zero = f(zero)

        if abs(f_zero) < err_max or abs(b - a) < err_max:
            return zero, it + 1
        
        if f(a)*f_zero < 0:
            b = zero
        else:
            a = zero

    return zero, it + 1


def zero_bisection_plot(f, a, b, err_max, it_max, plot_speed):

    x = np.linspace(a, b, 100)
    f_x = f(x)
    f_min = min(f_x)
    f_max = max(f_x)

    plt.plot(x, f_x, 'b', [a, b], [0, 0], 'k')
    plt.plot([a, a], [f_min, f_max], 'r', [b, b], [f_min, f_max], 'r')

    for it in range(it_max):
        zero = (a + b)/2
        f_zero = f(zero)

        plt.plot([zero, zero], [f_min, f_max], 'g', zero, f_zero, 'go')

        if abs(f_zero) < err_max or abs(b - a) < err_max:
            break

        plt.pause(1/plot_speed)
        
        if f(a)*f_zero < 0:
            b = zero
        else:
            a = zero

        plt.plot([zero, zero], [f_min, f_max], 'r', zero, f_zero, 'ro')

    plt.show()
    return zero, it
