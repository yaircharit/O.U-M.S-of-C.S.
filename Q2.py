import numpy as np
import matplotlib.pyplot as plt


def least_squares_poli(points):
    if (type(points) is list):
        points = np.vstack(points).T
    Y = np.matrix(np.vstack(points[1]))
    X = np.matrix([[x**2, x, 1] for x in points[0]])

    return ((X.T*X).I*X.T*Y).A1
    
    
DECIMALS_ROUND = 2
coords = [(1, 10), (2, 5.49), (3, 0.89), (4, -0.14), (5, -1.07), (6, 0.84)]
x,y = np.vstack(coords).T
a,b,c  = least_squares_poli(coords)
plt.plot(x,y,'o', label='Original Data')
x.sort()
x= np.linspace(x[0],x[-1],101)
plt.plot(x,a*x**2+b*x+c,'r', label=f'{round(a,DECIMALS_ROUND)}x^2 + {round(b,DECIMALS_ROUND)}x + {round(c,DECIMALS_ROUND)}')

plt.legend()
plt.show()