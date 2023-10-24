import pandas as pd
import numpy as np
from ann_comp_graph import *
from sklearn.neural_network import MLPClassifier

def one_hot_encoding(df, column):
    one_hot = pd.get_dummies(df[column], prefix=column)
    df = df.drop(column, axis=1)
    df = df.join(one_hot)

    return df

def train_test_split(df, percent):
    train=df.sample(frac=percent,random_state=200)
    test=df.drop(train.index)
    return train, test


def normalize_rows(df, rows):
    for row in rows:
        df[row] = (df[row]-df[row].min())/(df[row].max()-df[row].min())
    return df

if __name__ == "__main__":
    df = pd.read_csv("diabetes-prediction.csv")
    df=df.sample(n=1000,random_state=200)

    # TODO preprocesirati podatke

    # TODO podeliti podatke na train i test skup
    
    # TODO razdvojiti x i y

    # TODO implementirati model neuronske mreze

    # TODO trenirati mrezu - koristiti sklearn.neural_network.MLPClassifier 
    
    # print(clf.score(test_x, test_y))