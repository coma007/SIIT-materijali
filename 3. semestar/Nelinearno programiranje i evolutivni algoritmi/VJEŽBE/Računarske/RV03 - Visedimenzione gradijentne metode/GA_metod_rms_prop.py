from funkcija import *


def rms_prop(gradf, x0, gamma, omega, epsilon1, epsilon, it):

    x = np.array(x0).reshape(len(x0), 1)
    G = np.zeros(shape=x.shape)

    for i in range(it):
        g = gradf(x)
        G = omega * G + (1-omega) * np.multiply(g, g)
        tmp = gamma * np.ones(shape=G.shape) / np.sqrt(G+epsilon1)*g
        x = x - tmp
        if np.linalg.norm(x) < epsilon:
            break

    return x


if __name__ == '__main__':

    result = rms_prop(lambda x: df(x), [1, 2], 0.05, 0.9, 1e-6, 1e-6, 100)
    print("RMS PROP: ", result)
