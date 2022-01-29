from funkcija import *


def metod_sa_momentom(gradf, x0, gamma, epsilon, omega, it):
    # omega - brzina

    x = np.array(x0).reshape(len(x0), 1)
    v = np.zeros(shape=x.shape)

    for i in range(it):
        g = gradf(x)
        v = omega * v + gamma * g
        x = x - v
        if np.linalg.norm(g) < epsilon:
            break

    return x


if __name__ == '__main__':

    result = metod_sa_momentom(lambda x: df(x), [1, 2], 0.05, 0.0001, 0.5, 100)
    print("Metod sa momentom: ", result)
