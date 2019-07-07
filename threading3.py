import numpy as np
import matplotlib.pyplot as plt
N = 100
x_zeros = np.random.multivariate_normal(mean=np.array((-1,-1)),cov=.1*np.eye(2),size=(N/2))
y_zeros = np.zeros((N/2,))

x_ones = np.random.multivariate_normal(mean=np.array((1,1)),cov=.1*np.eye(2),size=(N/2))
y_ones=np.nes((N/2,))


x_np = np.vstack([x_zeros,x_ones])
y_np=np.concatenate([y_zeros,y_ones])

plt.plot(x_np,y_np)

