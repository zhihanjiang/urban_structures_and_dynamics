# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 20:28:15 2018

@author: 305
"""

import numpy
from matplotlib import pyplot
from pandas import read_csv

# load data

dataframe = read_csv("GP_means.csv", header=None, dtype=numpy.float64)
# dataframe = read_csv("../data/fake.csv", header=None)

#pyplot.plot(dataset1)
#pyplot.savefig('huizhan_grids1.png')
#pyplot.show()
#dataset5 = dataframe.values[:,87]
#dataset6 = dataframe.values[:,62]
#X5 = dataset5.transpose()
#X6 = dataset6.transpose()
for i in range(0,147):
    dataset = dataframe.values[:,i]
    X = dataset.transpose() #将dataset矩阵转置
    size = 24*7
    pyplot.plot(X,'orangered')
    #pyplot.legend(loc='upper right')
    #pyplot.xlabel('Days')
    #pyplot.ylabel('Traffic Volume')
    pyplot.xticks(numpy.arange(0, size, 24),  ('MON','TUE','WED','THU','FRI','SAT','SUN'))
    pyplot.gca().xaxis.grid(True)
    pyplot.savefig('area_TP%s.png'%(i), bbox_inches= 'tight', transparent = True, dpi=600)#生成每个区域格子的流量画像曲线area traffic profile
    pyplot.show()

#pyplot.plot(X6,'y',label='convention center')
#pyplot.legend(loc='upper right')
#pyplot.xlabel('Days')
#pyplot.ylabel('Traffic Volume')
#pyplot.xticks(numpy.arange(0, size1, 24),  ('MON','TUE','WED','THU','FRI','SAT','SUN'))
#pyplot.gca().xaxis.grid(True)
#pyplot.savefig('convention centergrids.png',dpi=300)
#pyplot.show()