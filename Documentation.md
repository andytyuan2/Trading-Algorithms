# Documentation for the pair trading algorithm I am making from scratch

## things to figure out 
- how to identify correlated stocks from outside of industry 

### I plan to use libraries such as numpy and yfinance
Topics that I will use will likely be: 
- geometric brownian motion
- monte carlo simulations

## Steps that I am currently planning now:
1. obtain a historical year daily price list of a specific sector
   > might need to make a master list in another file
2. could either choose your own two stocks (Skip to step 7) or do a computationally heavy process as follows
4. for each stock, create another list that is the percentage change between daily prices
5. then, compare each stock by calculating a quotient of the two percentage changes per day
6. take the result that has the lowest standard deviation, which shows that the pair of stocks tend to trade at a similar level
7. for the two stocks, execute a geometric brownian motion simulation independently
8. select portions of the stock price where the slope of the line of best fit at that point diverge from the comparison stock
9. the way that i believe i should select which places is calculating s historical average price for each stock, then placing a conditional to invest if one moves +2 sd of historical price average + slope(time) and one moves -2 sd from their respective 'average' price. the historical average will have to be a line with a slope of expected return and y intercept of historical average price. the movement criteria will be based off this line
10. for this to work, the expected returns of both stocks should also be very similar, something i already check for in thr previous steps. 
11. to profit, you would short the one with positive slope and go long on the one with a negative slope, the divergence has to be large for there to be a substantial profit


## pairs trading concept
Pairs trading theory uses statistical arbitrage to create profit off of two or more stocks that move similarly. With just two stocks, for example GOOG and GOOGL, we expect them to trend similarly whether it is due to them being in the same industry, being the same company double listed, or some other outside influence. This relationship is usually seen just from historical data, so the pairs trading strategy has its setbacks if the stocks end up not having that same relationship. 

The two stocks, since they are correlated, will tend to move similarly. This introduces the concept of mean reversion; an idea that stocks will tend to move slowly and steadily over time with the daily movements being non-vital to the overarching performance of the stock. Pairs trading aims to take advantage of the daily movements within interrelated stocks. When the group of stocks begins to move away from this mean, a trader would take appropriate action based on the direction of movement of each stock. 

For stocks that are trending downwards away from the mean, the trader would hold a long position so that they will see a profit when the stock goes back up. On the opposite side, for stocks trending upwards away from the mean, the trader would open a short position so that they will profit from a movement downwards. This combination of profits both up and down is what makes pair trading so popular. 

of course, actually making a profit will involve more advanced signals, infrastructure, speed, and luck, but the basic concept will be demonstrated with the script here. 


## setting the stage for the demonstration 

 
   
