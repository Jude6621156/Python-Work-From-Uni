import pandas as pd

ds1 = pd.read_csv('http://raptor.kent.ac.uk/~ds756/Data/kc_house_data_small.csv')
ds1['unit_price'] = ds1.price / ds1.sqft_living
