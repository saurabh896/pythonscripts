# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 19:00:37 2019

@author: User
"""

import pandas as pd

a=pd.read_csv("master.csv")


b=a["suicides_no"].max()
c=a[a["suicides_no"]==b]
print(c)

a_new=a[(a["country"]=="Japan") & (a["sex"]=="male")]
print(a_new)
print(a_new["suicides_no"].sum())
print(a_new["suicides_no"].mean())
