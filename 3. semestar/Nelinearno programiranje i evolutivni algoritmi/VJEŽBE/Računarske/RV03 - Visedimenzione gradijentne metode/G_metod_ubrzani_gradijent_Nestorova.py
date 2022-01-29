from funkcija import *


def ubrzani_gradijent_Nestorova(gradf, x0, gamma, epsilon, omega, it):

    x = np.array(x0).reshape(len(x0), 1)
    v = np.zeros(shape=x.shape)

    for i in range(it):
        x_est = x + omega*v
        g = gradf(x_est)
        v = gamma * g + omega * v
        x = x - v
        if np.linalg.norm(g) < epsilon:
            break

    return x


if __name__ == '__main__':

    result = ubrzani_gradijent_Nestorova(lambda x: df(x), [1, 2], 0.05, 0.0001, 0.5, 100)
    print("Ubrzani gradijent Nestorova: ", result)
