import numpy as np
import matplotlib.pyplot as plt


DECIMALS_ROUND = 2
coords = [(1, 10), (2, 5.49), (3, 0.89), (4, -0.14), (5, -1.07), (6, 0.84)]
x, y = np.vstack(coords).T
Y = np.matrix(np.vstack(y))
X = np.matrix([[x**2, x, 1] for x in x])

a, b, c = ((X.T*X).I*X.T*Y).A1
plt.plot(x, y, 'o', label='Original Data')
x.sort()
x = np.linspace(x[0], x[-1], 101)
plt.plot(x, a*x**2+b*x+c, 'r',
         label=f'{round(a,DECIMALS_ROUND)}x^2 + {round(b,DECIMALS_ROUND)}x + {round(c,DECIMALS_ROUND)}')

plt.legend()
plt.show()
