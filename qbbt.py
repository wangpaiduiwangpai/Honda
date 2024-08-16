import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(x):
    return np.sin(x)

# Define the range of x
x = np.linspace(-np.pi, np.pi, 1000)

# Plot the function
plt.plot(x, f(x))


# Define the range of x
x = np.linspace(-np.pi, np.pi, 1000)

# Plot the function
plt.plot(x, f(x))

# Set the x and y limits
plt.xlim(-np.pi, np.pi)
plt.ylim(-1.5, 1.5)

# Set the x and y labels
plt.xlabel('x')
plt.ylabel('f(x)')

# Show the plot
plt.show()
