# -*- coding: utf-8 -*-
"""
Created on Sun May 12 11:29:18 2019

@author: User
"""

from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from sklearn.tree import export_graphviz
import pydot
from  sklearn.ensemble import RandomForestRegressor

features=pd.read_csv('temps.csv')

print(features.head(5))


features=pd.get_dummies(features)
print(features.iloc[:,5:].head(5))

labels=np.array(features['actual'])
features=features.drop('actual',axis=1)
features_list=list(features.columns)
features=np.array(features)

train_features,test_features,train_lables,test_labels=train_test_split(features,labels,test_size=0.25,random_state=42)
baseline_preds=test_features[:,features_list.index('average')]
baseline_err=abs(baseline_preds-test_labels)

rf=RandomForestRegressor(n_estimators=1000,random_state=42)
rf.fit(train_features,train_lables)

predictions=rf.predict(test_features)

errors=abs(predictions-test_labels)

print('MAE',round(np.mean(errors),2),'degrees.')


mape=100*(errors/test_labels)
accracy=100-np.mean(mape)
print('Accracy',round(accracy,3),'%')
tree=rf.estimators_[5]
export_graphviz(tree,out_file='tree.dot',feature_names=features_list,rounded=True,precision=1)




(graph,)=pydot.graph_from_dot_file('tree.dot')
graph.write_png('tree.png')














