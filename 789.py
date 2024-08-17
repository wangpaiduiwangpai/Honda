import matplotlib.pyplot as plt
import numpy as np
import mpl_toolkits.mplot3d.axes3d as p3

fig = plt.figure()
ax = p3.Axes3D(fig,auto_add_to_figure=False)
fig.add_axes(ax)    

# prepare the data
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)


# plot the surface
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')


# set the axis limits
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
ax.set_zlim(-1, 1)


# show the plot
plt.show()