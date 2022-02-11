import numpy as np
from matplotlib import pyplot as plt


def zero_false_position(f, a, b, err_max=0.0001, it_max=100, plot_speed=-1):
    if f(a)*f(b) > 0:
        raise Exception('Invalid input: f(a)*f(b) > 0!')

    if plot_speed <= 0:
        return zero_false_position_no_plot(f, a, b, err_max, it_max)
    
    return zero_false_position_plot(f, a, b, err_max, it_max, plot_speed)


def zero_false_position_no_plot(f, a, b, err_max, it_max):
    for it in range(it_max):
        f_a = f(a)
        f_b = f(b)
        zero = b - f_b*(b - a)/(f_b - f_a)

        f_zero = f(zero)

        if abs(f_zero) < err_max or abs(b - a) < err_max:
            return zero, it

        if f_a*f_zero < 0:
            b = zero
        else:
            a = zero

    return zero, it

def zero_false_position_plot(f, a, b, err_max, it_max, plot_speed):

    x = np.linspace(a, b, 100)
    f_x = f(x)
    f_min = min(f_x)
    f_max = max(f_x)
    plt.plot(x, f_x, 'b', [a, b], [0, 0], 'k')

    for it in range(it_max):
        fA = f(a)
        fB = f(b)
        zero = b - fB*(b - a)/(fB - fA)
        plt.plot([a, b], [fA, fB], 'r', zero, 0, 'rx')

        fZero = f(zero)
        
        plt.plot([zero, zero], [f_min, f_max], 'g', zero, fZero, 'og')

        if abs(fZero) < err_max or abs(b - a) < err_max:
            break

        plt.pause(1/plot_speed)

        if fA*fZero < 0:
            b = zero
        else:
            a = zero
            
        plt.plot([zero, zero], [f_min, f_max], 'r', zero, fZero, 'og')

    plt.show()
    return zero, it + 1
