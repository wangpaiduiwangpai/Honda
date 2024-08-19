import mpl_toolkits.mplot3d as a3
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = a3.Axes3D(fig,auto_add_to_figure=False)
fig.add_axes(ax)

X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'))

plt.show()