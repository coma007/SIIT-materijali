from funkcija import *


def adagrad(gradf, x0, gamma, epsilon1, epsilon, it):

    x = np.array(x0).reshape(len(x0), 1)
    G = np.zeros(shape=x.shape)

    for k in range(it):
        g = gradf(x)
        G = G + np.multiply(g, g)
        tmp = gamma * np.ones(shape=G.shape) / np.sqrt(G+epsilon1) * g
        x = x - tmp
        if (np.linalg.norm(g)) < epsilon:
            break

    return x


if __name__ == '__main__':

    result = adagrad(lambda x: df(x), [1, 2], 0.2, 1e-6, 1e-6, 100)
    print("ADAGRAD: ", result)
