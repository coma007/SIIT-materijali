from funkcija import *


def metod_najbrzeg_pada(gradf, x0, gamma, epsilon, it):
    # gamma - learning rate
    # epsilon - toleracija

    x = np.array(x0).reshape(len(x0), 1)

    for i in range(it):
        g = gradf(x)
        x = x - gamma * g
        if np.linalg.norm(g) < epsilon:
            break
    return x


def metod_najbrzeg_pada_fiks(gradf, x0, gamma, epsilon, it):
    # gamma - learning rate
    # epsilon - toleracija

    x = np.array(x0).reshape(len(x0), 1)

    for i in range(it):
        g = gradf(x)
        x = x - gamma / np.linalg.norm(g) * g
        if np.linalg.norm(g) < epsilon:
            break
    return x


if __name__ == '__main__':

    result = metod_najbrzeg_pada(lambda x: df(x), [1, 2], 0.2, 0.0001, 100)
    print("Metod najbrzeg pada: ", result)
    result = metod_najbrzeg_pada_fiks(lambda x: df(x), [1, 2], 0.2, 0.0001, 100)
    print("Metod najbrzeg pada sa fiksnim korakom: ", result)
