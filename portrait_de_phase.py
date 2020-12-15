import numpy as np
import matplotlib.pyplot as plt

alpha = 0.7
beta = 0.7
gamma = 0.7
delta = 0.7

x1 = np.arange(0, 2.2, 0.1)
x2 = np.arange(0, 2.2, 0.1)

X1, X2 = np.meshgrid(x1, x2)
u = X1*(alpha - beta*X2)
v = -X2*(gamma - delta*X1)

fig, ax = plt.subplots()

ax.streamplot(X1, X2, u, v, density=1)
ax.axis([0.5, 2.1, 0, 2])
ax.xaxis.set_ticks([])
ax.yaxis.set_ticks([])
ax.set_title('portrait de phase')

plt.show()
