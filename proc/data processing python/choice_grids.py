# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 16:01:02 2017

@author: 305
"""

import numpy
from matplotlib import pyplot
from pandas import read_csv
from sklearn.metrics import mean_absolute_error
from statsmodels.graphics.tsaplots import plot_acf,plot_pacf
from statsmodels.tsa.arima_model import ARIMA

# load data

dataframe = read_csv("NGrids.csv", header=None, dtype=numpy.float64)
# dataframe = read_csv("../data/fake.csv", header=None)
error_matrix= []

#pyplot.plot(dataset1)
#pyplot.savefig('huizhan_grids1.png')
#pyplot.show()
#dataset5 = dataframe.values[:,87]
#dataset6 = dataframe.values[:,62]
#X5 = dataset5.transpose()
#X6 = dataset6.transpose()


dataset1 = dataframe.values[:,0]
dataset2 = dataframe.values[:,1]
dataset3 = dataframe.values[:,2]
dataset4 = dataframe.values[:,3] 
X1 = dataset1.transpose() #将dataset矩阵转置
X2 = dataset2.transpose()
X3 = dataset3.transpose()
X4 = dataset4.transpose()
size = 24*11 
size1 = 24*7

#pyplot.plot(X5,'r',label='railway station')
#pyplot.legend(loc='upper right')
#pyplot.xlabel('Days')
#pyplot.ylabel('Traffic Volume')
#pyplot.xticks(numpy.arange(0, size1, 24),  ('MON','TUE','WED','THU','FRI','SAT','SUN'))
#pyplot.gca().xaxis.grid(True)
#pyplot.savefig('railway stationgrids.png',dpi=300)
#pyplot.show()
#
#pyplot.plot(X6,'y',label='convention center')
#pyplot.legend(loc='upper right')
#pyplot.xlabel('Days')
#pyplot.ylabel('Traffic Volume')
#pyplot.xticks(numpy.arange(0, size1, 24),  ('MON','TUE','WED','THU','FRI','SAT','SUN'))
#pyplot.gca().xaxis.grid(True)
#pyplot.savefig('convention centergrids.png',dpi=300)
#pyplot.show()

pyplot.subplot(211)
pyplot.plot(X1, 'r', label='convention center1')
pyplot.legend(loc='upper right')
pyplot.xlabel('Days')
pyplot.ylabel('Traffic Volume')
pyplot.xticks(numpy.arange(0, size1, 24), ('MON','TUE','WED','THU','FRI','SAT','SUN'))
pyplot.gca().xaxis.grid(True)
   
pyplot.subplot(212)
pyplot.plot(X2, 'g', label='convention center2')
pyplot.legend(loc='upper right')
pyplot.xlabel('Days')
pyplot.ylabel('Traffic Volume')
 
pyplot.xticks(numpy.arange(0, size1, 24), ('MON','TUE','WED','THU','FRI','SAT','SUN'))
pyplot.gca().xaxis.grid(True)
 
pyplot.savefig('会展区块.png',dpi=300)
pyplot.show()
#
#
pyplot.subplot(211)
pyplot.plot(X3, 'b', label='railway station1')
pyplot.legend(loc='upper right')
pyplot.xlabel('Days')
pyplot.ylabel('Traffic Volume')
pyplot.xticks(numpy.arange(0, size1, 24), ('MON','TUE','WED','THU','FRI','SAT','SUN'))
pyplot.gca().xaxis.grid(True)
   
pyplot.subplot(212)
pyplot.plot(X4, 'm', label='railway station2')
pyplot.legend(loc='upper right')
pyplot.xlabel('Days')
pyplot.ylabel('Traffic Volume')
 
pyplot.xticks(numpy.arange(0, size1, 24), ('MON','TUE','WED','THU','FRI','SAT','SUN'))
pyplot.gca().xaxis.grid(True)

pyplot.savefig('火车区块.png',dpi=300)
pyplot.show()


#========================================================================