import pandas as pd

data= pd.read_csv(r'C:\Users\Admin\Downloads\data_science_new\python_lib\pokemon_data.csv')
print(data.head())
print(data.dtypes)
print(data.info())
