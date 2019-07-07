# -*- coding: utf-8 -*-
"""
Created on Mon May 27 19:16:53 2019

@author: User
"""
from pandas.tools.plotting import scatter_matrix
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import matplotlib.pyplot as plt
encoder=LabelEncoder()
housing=pd.read_csv('housing.csv')
print(pd.DataFrame(housing))

attributes=["median_house_value","median_income","total_rooms","housing_median_age"]
print(scatter_matrix(housing[attributes]))

#housing.plot(kind="scatter",x="longitude",y="latitude",alpha=0.4,s=housing["population"]/100,label="population",c="median house value",cmap=plt.get_cmap("jet"),colorbar=True)
#housing.plot(kind="scatter", x="longitude", y="latitude", alpha=0.4,
#s=housing["population"]/100, label="population",
#c="median_house_value", cmap=plt.get_cmap("jet"), colorbar=True,
#)
#plt.legend()
