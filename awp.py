import matplotlib.pyplot as plt
import numpy as np


def plot_graph(x, y):
    plt.plot(x, y)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Graph')
    plt.show()


def main():
    x = np.arange(0, 10, 0.1)
    y = np.sin(x)
    plot_graph(x, y)


if __name__ == '__main__':
    main()
    