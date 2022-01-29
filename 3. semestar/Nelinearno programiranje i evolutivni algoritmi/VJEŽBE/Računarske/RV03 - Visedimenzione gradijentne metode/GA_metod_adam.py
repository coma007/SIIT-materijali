from funkcija import *


def adam(gradf, x0, gamma, omega1, omega2, epsilon1, epsilon, it):

    x = np.array(x0).reshape(len(x0), 1)
    v = np.zeros(shape=x.shape)
    m = np.zeros(shape=x.shape)

    for i in range(it):
        g = gradf(x)
        m = omega1 * m + (1-omega1) * g
        v = omega2 * v + (1-omega2) * np.multiply(g, g)
        m_hat = m / (1 - omega1)
        v_hat = v / (1 - omega2)
        tmp = gamma / np.sqrt(v_hat + epsilon1) * m_hat
        x = x - tmp
        if np.linalg.norm(g) < epsilon:
            break

    return x


if __name__ == '__main__':

    result = adam(lambda x: df(x), [1, 2], 0.1, 0.1, 0.9, 1e-6, 1e-6, 100)
    print("ADAM: ", result)
