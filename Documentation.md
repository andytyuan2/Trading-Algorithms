# Documentation for the pair trading algorithm I am making from scratch

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
9. to profit, you would short the one with positive slope and go long on the one with a negative slope, the divergence has to be large for there to be a substantial profit


 ## pairs trading theory 

 
   
