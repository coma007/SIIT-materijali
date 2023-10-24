import pandas as pd
import numpy as np
from sklearn.metrics import f1_score


# METRIKA
# y_pred -> predikcije vaseg modela
# y_test -> prave vrednosti iz csv
F1 = f1_score(y_pred, y_test, average='micro')
print(f'F1: {F1}')
