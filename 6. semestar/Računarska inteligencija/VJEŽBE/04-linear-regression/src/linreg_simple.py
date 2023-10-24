import random
import matplotlib.pyplot as plt


def fit(x, y):
    assert len(x) == len(y)
    slope = 0.0  # nagib linije
    intercept = 0.0  # tacka preseka na y-osi
    # TODO 1: implementirati linearnu regresiju, y = ax + b, y = slope * x + interceptju

    return slope, intercept


def predict(x, slope, intercept):
    # TODO 2: prediktuj vrednosti y na osnovu jednog podatka x koristeci nagib i presek
    return 0


def make_predictions(x, slope, intercept):
    y_pred = [predict(xi, slope, intercept) for xi in x]
    return y_pred


if __name__ == '__main__':
    # da rezultati mogu da se reprodukuju
    random.seed(1337)  
    # random generisi podatke sa nasumicnim sumom
    x = [xi for xi in range(50)]
    # y = x (+- nasumicni sum)
    y = [(xi + random.randint(-5, 5)) for xi in x]  

    # izracunaj nagib i presek za liniju koja se najbolja uklapa (best fit)
    slope, intercept = fit(x, y)

    # prediktuj y za svako x
    y_pred = make_predictions(x, slope, intercept)

    # plotuj podatke i liniju koja se nabolje uklapa (best fit)
    plt.plot(x, y, '.')
    plt.plot(x, y_pred, 'b')
    plt.title(f'slope: {slope:.2f}, intercept: {intercept:.2f}')
    plt.show()
