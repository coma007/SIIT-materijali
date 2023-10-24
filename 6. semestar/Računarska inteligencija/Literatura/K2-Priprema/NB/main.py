import pandas as pd
from sklearn.base import accuracy_score
import spacy # biblioteka za procesiranje teksta

# METRIKA
accuracy = accuracy_score(y_pred, y_test)
print(f'Accuracy: {accuracy}')
