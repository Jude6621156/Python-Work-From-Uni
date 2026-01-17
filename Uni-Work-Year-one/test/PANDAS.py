import pandas as pd

ds1 = pd.read_csv('http://raptor.kent.ac.uk/~ds756/Data/heart.csv', index_col = "RestingBP")
ds1 = ds1.sort_values('Age')
k = ds1.Age.max()
ds1['AgeNorm'] = ds1.Age / ds1.Age.max()
