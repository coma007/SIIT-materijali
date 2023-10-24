import pandas as pd
import numpy as np
from ann_comp_graph import *


def one_hot_encoding(df, column):
    one_hot = pd.get_dummies(df[column], prefix=column)
    df = df.drop(column, axis=1)
    df = df.join(one_hot)

    return df

def train_test_split(df, percent):
    train=df.sample(frac=percent,random_state=200)
    test=df.drop(train.index)
    return train, test

def predict_mse(nn, test_x, test_y):
    total = 0
    for x, y in zip(test_x, test_y):
        res = nn.predict(x)
        total += (res-y)**2
        print(res, y)
    return total/len(test_x)

def normalize_rows(df, rows):
    for row in rows:
        df[row] = (df[row]-df[row].min())/(df[row].max()-df[row].min())
    return df

if __name__ == "__main__":
    df = pd.read_csv("life-expectancy.csv")
    df = df.sample(n=1000,random_state=200)
    df = df.drop('Country', axis=1)
    # TODO preprocesirati podatke

    # TODO podeliti podatke na train i test skup
    
    # TODO razdvojiti x i y

    # TODO implementirati model neuronske mreze

    # TODO trenirati mrezu

    # print(predict_mse(nn, test_x, test_y))