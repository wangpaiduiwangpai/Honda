import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import numpy as np

fig = plt.figure()
ax = p3.Axes3D(fig)

# prepare the data
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)


# plot the surface
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')

# set the axis labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D surface plot')


plt.show()











 