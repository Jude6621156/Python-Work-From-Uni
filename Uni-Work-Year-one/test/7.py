import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
from sklearn.model_selection import train_test_split
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
s = data.select_dtypes(include='int').columns
data[s] = data[s].astype("float")
d = e.fit_transform(data.loc[:, ['Gender']])
data['Female'] = d[:, 0]
data['Male'] = d[:, 1]
data = data.drop(columns=['Gender'])
f = ['TB Total Bilirubin', 'DB Direct Bilirubin', 'Alkphos Alkaline Phosphotase']
x = data.loc[:, 'Female':'Male']
y = data['Class']
X_train, X_test, y_train, y_test = train_test_split(x, y, random_state=0)

#x_train = data.loc[:, "Age":"TB Total Bilirubin"]
t = DecisionTreeClassifier()
t.fit(X_train, y_train)

#pwe = plt.figure(figsize=(25,20))
#_=plot_tree(t, feature_names = columns, class_names='hi', filled=True)
print(t.score(X_test, y_test))
