# Stock Volatility

### Description

This program analyzes the volatility of stocks versus that of the S&P 500. 

`Note:` This analysis should not be used for investment purposes.

### Functionality

- Enter the stock tickers that you wish to analyze separated by whitespace.
- Enter the year, day, and month from which to begin analysis as prompted.
- Enter the year, day, and month at which to end analysis as prompted.
- The annual, monthly, weekly, and daily volatility of the S&P 500 and each requested stock 
will be printed to the console.
- A plot of the daily volatility of the S&P 500 and all requested stock will be displayed.

### Imports

This program uses the *pandas* library to manipulate large datasets and the *pandas-datareader* module to
parse stock data from Yahoo Finance. It also uses the *datetime* module to set the date range to analyze.
Additionally, it uses the Matplotlib library to visualize the analyzed data. Finally, it uses the *math* module to
perform some mathematical calculations.

### Example Output

![](img/aapl_tsla_example.png?raw=true "Apple and Tesla")
![](img/msft_example.png?raw=true "Microsoft")
![](img/console_output.png?raw=true "Console Output")

### GitHub

The GitHub repository for this project can be found [here](https://github.com/mjschwarz/StockVolatility.git).
