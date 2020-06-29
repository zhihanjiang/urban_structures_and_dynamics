# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 13:36:55 2018

@author: 305
"""

import pandas as pd  
from sklearn.cluster import KMeans  
import matplotlib.pyplot as plt 
from math import sqrt 
  
df_features = pd.read_csv(r'C:\Users\305\Desktop\kaiti\python processing\AGP.csv',encoding='gbk') # 读入数据  
'利用SSE选择k'  
SSE = []  # 存放每次结果的误差平方和  
for k in range(1,10):  
    estimator = KMeans(n_clusters=k)  # 构造聚类器  
    estimator.fit(df_features)  
    SSE.append(sqrt(estimator.inertia_))  
X = range(1,10)  
plt.xlabel('k')  
plt.ylabel('SSE')  
plt.plot(X,SSE,'o-')  
plt.show() 