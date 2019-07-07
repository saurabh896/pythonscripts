
import pandas as pd
from sklearn import datasets,linear_model
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
import numpy as np
##data=pd.read_csv("PRSA_data_2010.1.1-2014.12.31.csv")
##print(pd.DataFrame(data))
columns ="age sex bmi map tc ldl hdl tch ltg glu".split()

diabetes = datasets.load_diabetes()


df=pd.DataFrame(diabetes.data,columns=columns)

y=diabetes.target

print(y)


X_train,X_test,y_train,y_test=train_test_split(df,y,test_size=0.2)

lm = linear_model.LinearRegression()


model = lm.fit(X_train,y_train)

predictions = lm.predict(X_test)

plt.scatter(y_test,predictions)

plt.xlabel("True Values")

plt.ylabel("prediction")

print(model.score(X_train,y_train))

plt.plot(X_train,y_train)


print(model.score(X_train,y_train))



print(predictions[:5])

dataset=df.to_csv()