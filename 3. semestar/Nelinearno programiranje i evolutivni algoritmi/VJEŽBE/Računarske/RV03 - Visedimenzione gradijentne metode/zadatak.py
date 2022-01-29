import numpy as np
import sympy as sym
from G_metod_najbrzeg_pada import metod_najbrzeg_pada
from G_metod_sa_momentom import metod_sa_momentom
from G_metod_ubrzani_gradijent_Nestorova import ubrzani_gradijent_Nestorova
from GA_metod_adagrad import adagrad
from GA_metod_rms_prop import rms_prop
from GA_metod_adam import adam


def f(x):
    return x[0]**2 + 10 * x[1]**2


def df(x):
    x_sym = sym.Symbol('x')
    y_sym = sym.Symbol('y')
    f_sym = x_sym**2 + 10 * y_sym**2
    dfdx_sym = sym.diff(f_sym, x_sym)
    dfdy_sym = sym.diff(f_sym, y_sym)
    dfdx = sym.lambdify((x_sym, y_sym), dfdx_sym, 'numpy')
    dfdy = sym.lambdify((x_sym, y_sym), dfdy_sym, 'numpy')

    return np.array([dfdx(x[0], x[1]), dfdy(x[0], x[1])]).reshape(len(x), 1)


if __name__ == '__main__':

    result = metod_najbrzeg_pada(lambda x: df(x), [0.1, 0.2], 0.0005, 0.0001, 100)
    print("Metod najbrzeg pada: ", result)

    result = metod_sa_momentom(lambda x: df(x), [0.1, 0.2], 0.0005, 0.0001, 0.00005, 100)
    print("Metod sa momentom: ", result)

    result = ubrzani_gradijent_Nestorova(lambda x: df(x), [0.1, 0.2], 0.0005, 0.001, 0.005, 100)
    print("Ubrzani gradijent Nestorova: ", result)

    result = adagrad(lambda x: df(x), [0.1, 0.2], 0.0005, 1e-6, 1e-6, 100)
    print("ADAGRAD: ", result)

    result = rms_prop(lambda x: df(x), [0.1, 0.2], 0.0005, 0.09, 1e-6, 1e-6, 100)
    print("RMS PROP: ", result)

    result = adam(lambda x: df(x), [0.1, 0.2], 0.0005, 0.1, 0.09, 1e-6, 1e-6, 100)
    print("ADAM: ", result)
