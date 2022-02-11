import numpy as np
import matplotlib.pyplot as plt

def diameter(matrix):

    rows, cols = matrix.shape
    distance = -np.inf
    indices = ()

    for i in range(rows):
        for j in range(i+1, rows):
            temp_dist = np.sqrt(np.sum(np.square((matrix[i, :] - matrix[j, :]))))
            if temp_dist > distance:
                distance = temp_dist
                indices = (i, j)

    return round(distance, 4), indices


if __name__ == '__main__':

    points = np.array([[1.0, 0.0],
                        [4.0, 8.0],
                        [2.1, 1.2],
                        [3.2, 1.9],
                        [5.6, 4.3],
                        [7.9, 2.3],
                        [-1.0, 3.1]])

    print("Tačke: ", points)
    plt.scatter(points[:, 0], points[:, 1])
    diameter, indices = diameter(points)
    print("Maksimalna udaljenost: ", diameter)
    plt.scatter(points[indices[0], 0], points[indices[0], 1], color="red")
    plt.show()

