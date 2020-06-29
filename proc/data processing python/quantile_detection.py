# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 11:24:53 2018

@author: 305
"""

import numpy as np
from matplotlib import pyplot
from pandas import read_csv,Series


dataframe = read_csv("GP.csv", header=None, dtype=np.float64)
# dataframe = read_csv("../data/fake.csv", header=None)
for i in range(0,147):
    
    
    dataset = dataframe.values[:, i]

    # auto correlation
    X = dataset.transpose() #将dataset矩阵转置
    s = Series(X)
    q1= s.quantile(.25)#下四分位数
    q3 = s.quantile(.75)#上四分位数
    iqr = q3-q1#四分位差，IQR=Q3-Q1
    upper = q3+1.5*iqr
    lower = q1-1.5*iqr
    overflow = np.greater(X,upper)*X
    overflow[overflow == 0] = 'nan'
    underflow = np.less(X,lower)*X
    underflow[underflow == 0] = 'nan'


    #timeline = np.arange(0, len(X))
    
    #pyplot.fill_between(timeline, lower, upper, alpha=0.5, label='confidence')

    pyplot.plot(X,'k',label = 'groundtruth')
    pyplot.plot(overflow, 'r.', label='anomaly1', alpha=0.4)
    pyplot.plot(underflow, 'b.', label='anomaly2', alpha=0.5)
    pyplot.legend(loc = 'lower left')
    pyplot.xlabel('Days')
    pyplot.ylabel('Traffic Volume')
 
    pyplot.xticks(np.arange(0, len(X), 24), np.arange(1, 31))
    pyplot.gca().xaxis.grid(True)
    j = i+1
    pyplot.savefig('quan_anomaly%s.png'% (j), dpi=300)
    pyplot.show()
    
  
    