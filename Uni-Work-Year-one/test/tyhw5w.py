import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeClassifier

columns = ["Age",
 "Gender",
 "TB Total Bilirubin",
 "DB Direct Bilirubin",
 "Alkphos Alkaline Phosphotase",
 "Sgpt Alamine Aminotransferase",
 "Sgot Aspartate Aminotransferase",
 "TP Total Protiens",
 "ALB Albumin",
 "A/G Ratio Albumin / Globulin Ratio",
 "Class"]
data = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/00225/Indian%20Liver%20Patient%20Dataset%20(ILPD).csv', header = None, names = columns)
data = data.drop(data[data['A/G Ratio Albumin / Globulin Ratio'].isna()].index)
e = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
