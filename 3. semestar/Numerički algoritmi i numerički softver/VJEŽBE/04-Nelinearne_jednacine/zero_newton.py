import numpy as np
from matplotlib import pyplot as plt

def zero_newton(f, df, x0, err_max=0.0001, it_max=100, plot_speed=-1, plot_a=-5, plot_b=5):
    if df(x0) == 0:
        raise('Invalid input: df(x0) == 0!')
    
    if plot_speed <= 0:
        return zero_newton_no_plot(f, df, x0, err_max, it_max)
    
    return zero_newton_plot(f, df, x0, err_max, it_max, plot_speed, plot_a, plot_b)


def zero_newton_no_plot(f, df, x0, err_max, it_max):

    for it in range(it_max):
        zero = x0 - f(x0)/df(x0)

        f_zero = f(zero)
        if abs(f_zero) < err_max:
            return zero, it + 1
        
        x0 = zero

    return zero, it + 1

def zero_newton_plot(f, df, x0, err_max, it_max, plot_speed, plot_a, plot_b):
    
    x = np.linspace(plot_a, plot_b, 100)

    f_x = f(x)
    f_min = min(f_x)
    f_max = max(f_x)
    plt.plot(x, f_x, 'b', [plot_a, plot_b], [0, 0], 'k')

    for it in range(it_max):
        f_x0 = f(x0)
        zero = x0 - f_x0/df(x0)

        plt.plot([x0, zero], [f_x0, 0], 'r', zero, 0, 'rx')

        f_zero = f(zero)
        plt.plot([zero, zero], [f_min, f_max], 'g', zero, f_zero, 'go')

        if np.abs(f_zero) < err_max:
            break
        plt.pause(1/plot_speed)
        
        x0 = zero

        plt.plot([zero, zero], [f_min, f_max], 'r', zero, f_zero, 'ro')
        
    plt.show()
    return zero, it + 1