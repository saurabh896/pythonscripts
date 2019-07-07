# -*- coding: utf-8 -*-
"""
Created on Sun May 12 17:57:30 2019

@author: User
"""

from sklearn.ensemble import RandomForestClassifier
import numpy as  np
from sklearn.model_selection import train_test_split
from scipy.io import arff
import pandas as pd


data=arff.loadarff('Autism-Adolescent-Data.arff')
df=pd.DataFrame(data[0])
list(df)
df = df.apply(lambda x: x.astype(str).str.lower())
df = df.replace('yes', 1)
df = df.replace('no', 0)
df = df.replace('f', 1)
df = df.replace('m', 0)

xVar = list(df.loc[:,'A1_Score':'A10_Score']) + ['gender'] + ['jundice'] + ['austim']
yVar = df.iloc[:,20]
df2 = df[xVar]

X_train, X_test, y_train, y_test = train_test_split(df2, yVar, test_size=0.2)
print (X_train.shape, y_train.shape)
print (X_test.shape, y_test.shape)

clf=RandomForestClassifier(n_jobs=2,random_state=0)
clf.fit(X_train,y_train)
RandomForestClassifier(bootstrap=True,class_weight=None,criterion='gini',max_depth=None,max_features='auto',max_leaf_nodes=None,min_impurity_split=1e-07,min_samples_split=2,min_weight_fraction_leaf=0.0,n_estimators=10,n_jobs=2,oob_score=False,random_state=0,verbose=0,warm_start=False)
preds=clf.predict(X_test)
print(pd.crosstab(y_test, preds, rownames=['Actual Result'], colnames=['Predicted Result']))
