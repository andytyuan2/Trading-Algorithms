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
        stock_of_choice = yf.Ticker(self.ticker)
        historical_price_stock = list(round(stock_of_choice.history(start="2022-06-06", end="2022-06-14", interval="1d")['Close'], 3))
        return historical_price_stock
    
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
        return np.average(self.stocks())
    
    def average_change(self):
        return np.average(self.price_change())
    
    def line_equation(self):
        return f'The equation of the line of best fit is: y = {self.average_change()}x + {self.average_price()}'
    
    def price_average_plot(self):
        price_plotted = []
        for x in range(0, len(self.price_change())):
            price_plotted.append(self.average_price() + x*self.average_change())
        return price_plotted



