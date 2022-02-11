import numpy as np
from matplotlib import pyplot as plt


def zero_secant(f, a, b, err_max, it_max, plot_speed):

    if f(a) == f(b):
        raise Exception('Invalid parameters: f(a) == f(b)!')

    if plot_speed <= 0:
        return zero_secant_no_plot(f, a, b, err_max, it_max)
    
    return zero_secant_plot(f, a, b, err_max, it_max, plot_speed)


def zero_secant_no_plot(f, a, b, err_max, it_max):
    for i in range(it_max):
        f_a = f(a)
        f_b = f(b)
        zero = b - f_b*(b - a)/(f_b - f_a)

        f_zero = f(zero)

        if abs(f_zero) < err_max:
            return zero, i + 1
        
        a = b
        b = zero

    return zero, i + 1

def zero_secant_plot(f, a, b, err_max, it_max, plot_speed):
    
    x = np.linspace(a, b, 100)
    f_x = f(x)
    f_min = np.min(f_x)
    f_max = np.max(f_x)

    plt.plot(x, f_x, 'b', [a, b], [0, 0], 'k')

    for i in range(it_max):
        f_a = f(a)
        f_b = f(b)
        zero = b - f_b*(b - a)/(f_b - f_a)
        plt.plot([a, b], [f_a, f_b], 'r', zero, 0, 'rx')

        f_zero = f(zero)
        
        plt.plot([zero, zero], [f_min, f_max], 'g', zero, f_zero, 'og')

        if abs(f_zero) < err_max:
            break
        
        plt.pause(1/plot_speed)


        a = b
        b = zero

        plt.plot([zero, zero], [f_min, f_max], 'r', zero, f_zero, 'og')

    plt.show()
    return zero, i + 1


