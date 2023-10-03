# SECTOR BASED PAIRS TRADING ALGORITHM

# K MEANS CLUSTERING VISUALIZER

# https://openquant.co/blog/quantitative-finance-portfolio-projects

import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import statistics as stats
import random

list_of_stocks = ['GOOG', 'GOOGL', 'AAPL', 'IBM', 'TSLA', 'META', 'NFLX']

stdev_list = []
quotient_average_list = []
################################################################################################################################################################################################
ticker1 = (random.sample(list_of_stocks,k=len(list_of_stocks)))
stock1 = yf.Ticker(ticker1[i])
historical_price_stock1 = np.array(round(stock1.history(start="2022-06-06", end="2023-06-06", interval="1d")['Close'], 6))

price_changes1_list = []
for x in range(0, len(historical_price_stock1)-1):
    percent_change1 = (historical_price_stock1[x+1] - historical_price_stock1[x])/ historical_price_stock1[x]
    if percent_change1 == 0:
        price_changes1_list.append(0.000001)
    else:
        price_changes1_list.append(float(percent_change1))   
historical_price_changes_array1 = np.array(price_changes1_list)

stock1_average_price = np.average(historical_price_stock1)
stock1_average_percent_change = np.average(historical_price_changes_array1)
price_plot1 = []
for x in range(0,len(historical_price_changes_array1)):
    price_plot1.append(stock1_average_price + x*stock1_average_percent_change)
################################################################################################################################################################################################
ticker2 = (random.sample(list_of_stocks,k=len(list_of_stocks)))
stock2 = yf.Ticker(ticker2[i])
historical_price_stock2 = np.array(round(stock2.history(start="2022-06-06", end="2023-06-06", interval="1d")['Close'], 6))

price_changes2_list = []
for x in range(0, len(historical_price_stock2)-1):
    percent_change2 = (historical_price_stock2[x+1] - historical_price_stock2[x])/ historical_price_stock2[x]
    if percent_change2 == 0:
        price_changes2_list.append(0.000001)
    else:
        price_changes2_list.append(float(percent_change2))
historical_price_changes_array2 = np.array(price_changes2_list)

stock2_average_price = np.average(historical_price_stock2)
stock2_average_percent_change = np.average(historical_price_changes_array2)
price_plot2 = []
for x in range(0,len(historical_price_changes_array2)):
    price_plot2.append(stock2_average_price + x*stock2_average_percent_change)   # find way to show the equation of the line (y = slope*x + average_price)
################################################################################################################################################################################################
price_quotient = []    
for x,y in zip(historical_price_changes_array1, historical_price_changes_array2):
    price_quotient.append(y/x)

stdev_list.append(stats.stdev(price_quotient))
quotient_average_list.append(np.average(price_quotient))

print(ticker1)
print(ticker2)
print('standard deviation of quotient list is', stdev_list, "(should be near 0)")
print("average of quotient between", ticker1[0], "and", ticker2[0], "is", quotient_average_list, "(should be near 1)")

# need to find a way that this can be an exhaustive search that does not involve the same
    # could be from just doing a permutation and taking out the ones that have stdev 0 and quotient 1

