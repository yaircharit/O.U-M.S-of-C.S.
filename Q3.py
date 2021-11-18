import numpy as np
import matplotlib.pyplot as plt

# [(1,2),(3,3),(3,5),(5,4),(5,6),(6,5),(8,7),(9,8)]
data = [(1.1, 1.4), (1.5, 2.1), (1, 1.6), (2, 2.1), (2.3, 3.2),
        (3.1, 3.5), (1.9, 2.7), (2.2, 3.4), (0.5, 1.2), (2.5, 2.9)]
X, Y = np.vstack(data).T

xt = sum(X)/len(X)
yt = sum(Y)/len(Y)
cx = sum([(x-xt)**2 for x in X])/len(X)
cy = sum([(y-yt)**2 for y in Y])/len(Y)
cxy = sum([(x-xt)*(y-yt) for x, y in data])/len(Y)
covid = np.array([[cx, cxy], [cxy, cy]])

vals, vecs = np.linalg.eigh(covid)

X, Y = np.vstack(data).T
origin = [xt, yt]
spc = np.linspace(min(X)-0.5, max(X)+0.5, 101)

plt.xlim = [min(X)-1, max(X)+1]
plt.plot(X, Y, 'o', label='Original Data')
y = (vecs[1][1] * spc) / vecs[0][1]
plt.plot(spc, y, 'r')
y = (vecs[1][1] * X) / vecs[0][1]
plt.plot(X, y, 'o', label='Recovered Data')

#Show difference
for i in range(len(Y)):
    temp_y = np.linspace(y[i],Y[i],101) 
    temp_x = [X[i] for j in range(len(temp_y))]
    plt.plot(temp_x,temp_y,'g')

plt.legend()
plt.show()
