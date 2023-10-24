import pandas as pd
import numpy as np

def calculate_rmse(predicted, true):
    return np.sqrt(((predicted - true) ** 2).mean())

# METRIKA
# y_pred -> predikcije vaseg modela
# y_test -> prave vrednosti iz csv
RMSE = calculate_rmse(y_pred, y_test)
print(f'RMSE: {RMSE}') 
