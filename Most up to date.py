import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import statistics as stats
import random
import scipy as sp
gbm_length = 100

# Step 1: get a list of the stocks in a certain sector


class stock:
    def __init__(self, ticker):
        self.ticker = ticker
# Step 2: get a daily price list for desired interval       
    def stocks(self):
        stock_of_choice = yf.Ticker(self.ticker)
        historical_price_stock = list(round(stock_of_choice.history(period="5d", interval="30m")['Close'], 3))
        return historical_price_stock
    
# Step 3: list of percentage change between daily prices
    def price_change(self):
        price_changes_list = []
        for x in range(0, len(self.stocks())-1):
            percent_change = round((self.stocks()[x+1] - self.stocks()[x]) * 100 / self.stocks()[x], 3)
            if percent_change == 0:
                price_changes_list.append(0.0001)
            else:
                price_changes_list.append(percent_change)
        return price_changes_list
    
    def average_price(self):
        return float(np.average(self.stocks()))
    
    def price_std(self):
        return float(np.std(self.stocks()))
    
    def average_change(self):
        return float(np.average(self.price_change()))
    
    def price_average_plot(self):
        price_plotted = []
        for x in range(0, len(self.price_change())):
            price_plotted.append(self.average_price() + x*self.average_change())
        return price_plotted
    
    def geometric_brownian(self):
        price_list = [(self.stocks()[-1])]
        stock_vol = float(self.price_std() / self.average_price())
        expected_return = yf.Ticker(self.ticker).info['52WeekChange']
        for num in range(0,gbm_length):
            rng = np.random.default_rng().normal()
            change = expected_return*price_list[num]*1/len(self.stocks()) + stock_vol*math.sqrt(1/len(self.stocks()))*price_list[num]*rng
            new_price = price_list[num] + change
            price_list.append(new_price)
        return price_list
            
    def time_list(self):
        time_list = list(range(0,len(self.stocks())+1))
        return time_list
    
    def line_equation(self):
        line_list = [self.geometric_brownian()[0]]
        for i in range(1,len(self.stocks())+1):
            points = line_list[0] + i*(self.average_change())
            line_list.append(points)
        return line_list
    
    def standarddev(self):
        stdev = np.std(self.line_equation)
        return stdev            
        
    
stock1 = stock("KO")
stock2 = stock("PEP")

pair_trade_opps = []
for i in range(0, gbm_length):
    if (stock1.geometric_brownian()[i] >= (stock1.line_equation()[i] + 2*stock1.standarddev())) and (stock2.geometric_brownian()[i] <= (stock2.line_equation()[i] - 2*stock2.standarddev())):
        pair_trade_opps.append()
        print(f'pair trade opportunity at t = {i}!')
    elif (stock2.geometric_brownian()[i] >= (stock2.line_equation()[i] + 2*stock2.standarddev())) and (stock1.geometric_brownian()[i] <= (stock1.line_equation()[i] - 2*stock1.standarddev())):
        print(f'pair trade opportunity at t = {i}!')
    else: 
        print(f'Not a pair trade opportunity')

##### Step 4: compare stocks by calculating correlation of the price lists

# correlation = sp.stats.pearsonr(stock1.price_change(), stock2.price_change())
# print(correlation)



# two_stocks_quotient = []
# stock1_changes = stock1.price_change()
# stock2_changes = stock2.price_change()
# for i in range(0, len(stock1_changes)):
#     quotient = float(stock1_changes[i] / stock2_changes[i])
#     two_stocks_quotient.append(quotient)


