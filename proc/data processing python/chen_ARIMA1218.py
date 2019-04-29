# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 10:16:20 2017

@author: 305
"""

import numpy
from matplotlib import pyplot
from pandas import read_csv
from sklearn.metrics import mean_absolute_error
from statsmodels.graphics.tsaplots import plot_acf,plot_pacf
from statsmodels.tsa.arima_model import ARIMA

# %% load data
dataframe = read_csv("GP.csv", header=None, dtype=numpy.float64)
# dataframe = read_csv("../data/fake.csv", header=None)
dataset = dataframe.values[:, 13]
print(dataset.shape)

pyplot.plot(dataset)
pyplot.savefig('GP13.png')
pyplot.show()

# auto correlation
X = dataset.transpose() #将dataset矩阵转置
plot_acf(X, lags=24)
plot_pacf(X, lags=24)
pyplot.show()


# %%
size = 24 * 7
train, test = X[:size], X[size:len(X)]
forecast = numpy.zeros(len(test))
bound = numpy.zeros((len(test), 2))
step = 4
for t in range(0, len(test), step):
    print(t)
    model = ARIMA(train, order=(7, 0, 0))
    model_fit = model.fit()
    output = model_fit.forecast(step, alpha=.05)
    forecast[t:t + step] = output[0]
    bound[t:t + step, :] = output[2]  #???
    train = numpy.append(train, test[t:t + step])
error = mean_absolute_error(test, forecast)
print('Test MAE: %.3f' % error)


# %% plot
#==============================================================================
pyplot.show()
  
timeline = numpy.arange(0, len(test))
baseline = numpy.zeros(len(test))
residual = test - forecast
residual_1 = forecast-test

lower = bound[:, 0]
upper = bound[:, 1]
lower_1 = forecast-lower
overflow = numpy.greater(residual, upper) * residual
overflow[overflow == 0] = 'nan'
underflow = numpy.greater(residual_1, lower_1) * residual
underflow[underflow == 0] = 'nan'
  
pyplot.subplot(211)
pyplot.plot(test, 'g', label='groundtruth')
pyplot.plot(forecast, 'b', label='forecast')
#==============================================================================
  
pyplot.fill_between(timeline, lower, upper, alpha=0.5, label='confidence')
pyplot.legend()
pyplot.xlabel('Days')
pyplot.ylabel('Traffic Volume')
pyplot.xticks(numpy.arange(0, len(test), 24), numpy.arange(8, 31))
pyplot.gca().xaxis.grid(True)
   
pyplot.subplot(212)
pyplot.plot(timeline, baseline)
pyplot.plot(residual, 'k', label='residual')
pyplot.plot(overflow, 'r.', label='anomaly1', alpha=0.4)
pyplot.plot(underflow, 'b.', label='anomaly2', alpha=0.5)
pyplot.legend()
pyplot.xlabel('Days')
pyplot.ylabel('Traffic Volume')
 
pyplot.xticks(numpy.arange(0, len(test), 24), numpy.arange(8, 31))
pyplot.gca().xaxis.grid(True)
 
pyplot.savefig('anomaly_GP13.png', dpi=300)
pyplot.show()
#==============================================================================




