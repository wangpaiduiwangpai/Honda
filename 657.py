# 第1章/studyMatplotlib/3D图像.py
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# 用来正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

fig = plt.figure()
ax = Axes3D(fig)
X = np.arange(-1, 1, 0.01)
Y = np.arange(-1, 1, 0.01)
x1 = X.copy()
y1 = Y.copy()
X, Y = np.meshgrid(X, Y)
Z = (X ** 2 + Y ** 2 - (2 * X * Y))  # (x-y)**2
# 3d图像数据需要x,y,z 3个坐标
# rstride	数组行距（步长大小）
# cstride	数组列距（步长大小）
# color	    曲面块颜色映射
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')
plt.show()
# plt.savefig('3d_2图像')



