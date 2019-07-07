from sklearn.preprocessing import LabelEncoder
import pandas as pd
encoder=LabelEncoder()
housing=pd.read_csv('housing.csv')
housing_cat = housing["ocean_proxmity"]
print(housing_cat)