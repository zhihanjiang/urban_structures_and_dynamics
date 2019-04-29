# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 18:57:22 2018

@author: 305
"""

import numpy
from matplotlib import pyplot
from pandas import read_csv
import matplotlib

# load data
zhfont1 = matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\simsun.ttc')
dataframe = read_csv("GP_means.csv", header=None, dtype=numpy.float64)
# dataframe = read_csv("../data/fake.csv", header=None)
error_matrix= []

#pyplot.plot(dataset1)
#pyplot.savefig('huizhan_grids1.png')
#pyplot.show()
dataset5 = dataframe.values[:,87]
dataset6 = dataframe.values[:,62]
X5 = dataset5.transpose()
X6 = dataset6.transpose()


#dataset1 = dataframe.values[:,0]
#dataset2 = dataframe.values[:,1]
#dataset3 = dataframe.values[:,2]
#dataset4 = dataframe.values[:,3] 
#X1 = dataset1.transpose() #将dataset矩阵转置
#X2 = dataset2.transpose()
#X3 = dataset3.transpose()
#X4 = dataset4.transpose()
size = 24*11 
size1 = 24*7

pyplot.plot(X5,'r',label='火车站')
pyplot.legend(loc='upper right',prop=zhfont1)
pyplot.xlabel('时间', fontproperties=zhfont1)
pyplot.ylabel('交通流量', fontproperties=zhfont1)
pyplot.xticks(numpy.arange(0, size1, 24),  ('周一','周二','周三','周四','周五','周六','周日'),fontproperties=zhfont1)
pyplot.gca().xaxis.grid(True)
pyplot.savefig('火车站.png',dpi=300)
pyplot.show()
#
pyplot.plot(X6,'y',label='会展中心')
pyplot.legend(loc='upper right',prop=zhfont1)
pyplot.xlabel('时间', fontproperties=zhfont1)
pyplot.ylabel('交通流量', fontproperties=zhfont1)
pyplot.xticks(numpy.arange(0, size1, 24),  ('周一','周二','周三','周四','周五','周六','周日'),fontproperties=zhfont1)
pyplot.gca().xaxis.grid(True)
pyplot.savefig('会展中心.png',dpi=300)
pyplot.show()


#pyplot.subplot(211)
#pyplot.plot(X1, 'r', label='会展中心1')
#pyplot.legend(loc='upper right',prop=zhfont1)
##pyplot.xlabel('时间',fontproperties=zhfont1)
#pyplot.ylabel('交通流量', fontproperties=zhfont1)
#pyplot.xticks(numpy.arange(0, size1, 24), ('周一','周二','周三','周四','周五','周六','周日'),fontproperties=zhfont1)
#pyplot.gca().xaxis.grid(True)
#   
#pyplot.subplot(212)
#pyplot.plot(X2, 'g', label='会展中心2')
#pyplot.legend(loc='upper right',prop=zhfont1)
#pyplot.xlabel('时间',fontproperties=zhfont1)
#pyplot.ylabel('交通流量',fontproperties=zhfont1)
# 
#pyplot.xticks(numpy.arange(0, size1, 24), ('周一','周二','周三','周四','周五','周六','周日'),fontproperties=zhfont1)
#pyplot.gca().xaxis.grid(True)
# 
#pyplot.savefig('会展区块.png',dpi=300)
#pyplot.show()
##
##
#pyplot.subplot(211)
#pyplot.plot(X3, 'b', label='火车站1')
#pyplot.legend(loc='upper right',prop=zhfont1)
##pyplot.xlabel('Days',fontproperties=zhfont1)
#pyplot.ylabel('交通流量',fontproperties=zhfont1)
#pyplot.xticks(numpy.arange(0, size1, 24), ('周一','周二','周三','周四','周五','周六','周日'),fontproperties=zhfont1)
#pyplot.gca().xaxis.grid(True)
#   
#pyplot.subplot(212)
#pyplot.plot(X4, 'm', label='火车站2')
#pyplot.legend(loc='upper right',prop=zhfont1)
#pyplot.xlabel('时间',fontproperties=zhfont1)
#pyplot.ylabel('交通流量',fontproperties=zhfont1)
# 
#pyplot.xticks(numpy.arange(0, size1, 24), ('周一','周二','周三','周四','周五','周六','周日'),fontproperties=zhfont1)
#pyplot.gca().xaxis.grid(True)
#
#pyplot.savefig('火车区块.png',dpi=300)
#pyplot.show()
#
