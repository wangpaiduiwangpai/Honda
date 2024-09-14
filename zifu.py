import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号
x=pd.Series(np.exp(np.arange(20)))
x.plot(label=u'原始数据图',legend=True)
plt.grid(True)
plt.show()
x.plot(logy=True,label=u'对数数据图',legend=True) #这个函数里的参数logy=True时，是以10为底的
plt.grid(True)
plt.show()