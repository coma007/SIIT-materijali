import numpy as np


def stock_share(years, total_stocks):
    avg_stocks = total_stocks / np.sum(years)
    return np.round(avg_stocks * years)


if __name__ == '__main__':

    years = np.array([2, 3, 4, 6, 1, 2, 4, 8])
    sum = 1000
    stocks = stock_share(years, sum)
    print("stocks = ", stocks)
    print("sum = ", sum)
