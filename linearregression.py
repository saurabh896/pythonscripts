# -*- coding: utf-8 -*-
"""
Created on Mon May 27 19:58:48 2019

@author: User
"""

import numpy as np

x=2* np.random.rand(100,1)
y=4+3*x+np.random.rand(100,1)

x_b=np.c_[np.ones((100,1)),x]
theta_best=np.linalg.inv(x_b.T.dot(x_b)).dot(x_b.T).dot(y)
print(theta_best)