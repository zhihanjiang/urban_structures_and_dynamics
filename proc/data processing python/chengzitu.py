# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 19:49:25 2017

@author: 305
"""
import pandas as pd
import numpy as np
from matplotlib.ticker import MultipleLocator
import matplotlib.pyplot as plt
import xlrd
from xlrd import open_workbook
  

x_data=[]
y_data=[]
counts = 0
wb = open_workbook(r'C:\Users\305\Desktop\kaiti\tiyu.xlsx')
plt.figure(figsize=(25,20))
#fig=plt.figure()

for s in wb.sheets():
    for row in range(s.nrows):
        values = []
        for col in range(s.ncols):
            values.append(s.cell(row,col).value)
        x_data.append(values[0])
        y_data.append(values[1])
        counts+=1
        if counts%24==0:
            i=counts//24
            #plt.figure(figsize=(19, 12))
            #ax = plt.subplot(1, 1, 1) 
            plt.subplot(5,7,i+3)
            plt.plot(x_data,y_data,'-ob',linewidth=1,ms=2)
            plt.subplots_adjust(left=None,bottom=None,top=None,wspace=0.2,hspace=0.2)
            plt.xticks([z for z in range(0,23,2)],fontsize=10)
            plt.yticks([j for j in range(0,300,20)],fontsize=10)
            plt.grid(True)
            #xma = MultipleLocator(1)
            #ax.xaxis.set_major_locator(xma)
            plt.title(u'sep'+str(i))
            plt.legend()
#            plt.show()
            x_data=[]
            y_data=[]

#plt.show()
plt.savefig('tiyu.png',dpi=900)
#plt.savefig('./tu.jpg',format='jpg')