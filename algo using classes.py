import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import statistics as stats
import random

class stock:
    def __init__(self, ticker):
        self.ticker = ticker
        
    def stocks(self):
        stock = yf.Ticker(self.ticker)
        historical_price_stock = np.array(round(stock.history(start="2022-06-06", end="2023-06-06", interval="1d")['Close'], 6))
        return historical_price_stock
    
    def price_change(self):
        price_changes_list = []
        for x in range(0, len(self.stocks)-1):
            percent_change = (self.stocks[x+1] - self.stocks[x]) / self.stocks[x]
            if percent_change == 0:
                price_changes_list.append(0.000001)
            else:
                price_changes_list.append(float(percent_change))
        historical_price_change_array = np.array(price_changes_list)
        return historical_price_change_array
    
    def average(self):
        return np.average(self.stocks)
    
    def average_change(self):
        return np.average(self.price_change)
    
    def line_equation(self):
        print ('The equation of the line of best fit is: y = ', self.average_change, "x + ", self.average)
    
    def price_plot(self):
        price_plotted = []
        for x in range(0, len(self.price_change)):
            price_plotted.append(self.average + x*self.average_change)
        return price_plotted

p1 = stock("AAPL") 
print(p1.average())
print('The equation of the line of best fit is: y = ', p1.average_change(), "x + ", p1.average())
