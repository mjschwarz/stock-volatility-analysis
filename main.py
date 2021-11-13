import pandas as pd
import matplotlib.pyplot as plt
import glob


# ----------
# CONSTANTS
# ----------
SP_500 = 'stock_data/voo_historical_data.csv'
returns_interval = input('Enter the time interval at which to calculate returns (Yearly, Monthly, Weekly, Daily): ')


# -----------
# PLOT SETUP
# -----------
plt.style.use('seaborn-darkgrid')
plt.title('Stock Performance vs. S&P 500 (' + returns_interval + ')')
plt.xlabel('Time')
plt.ylabel('Returns')


# ---------------
# HELPER METHODS
# ---------------
def get_interval_returns(daily_returns, interval):
    """Calculates the stock returns at the given interval and plots the result.

    :param daily_returns: Pandas DataFrame
                        index: Datetime object representing the current date
                        column: daily stock returns data
    :param interval: str
                    time interval at which the calculate the stock returns (can be Y, M, W, D)
    """

    # calculate the weekly average return
    stock_returns_interval = daily_returns.resample(interval).mean()

    # plot monthly stock returns
    plt.plot(stock_returns_interval.index, stock_returns_interval,
             label='S&P 500' if file == SP_500 else file.split("stock_data/")[1].split("_")[0],
             alpha=0.8 if file == SP_500 else 0.6,
             zorder=10 if file == SP_500 else 0)


# ------------------
# DATA MANIPULATION
# ------------------
for file in glob.glob('stock_data/*'):
    # read in data from csv file
    stock_price_daily = pd.read_csv(file,
                                    usecols=['Date', 'Close/Last'],
                                    parse_dates=['Date'],
                                    infer_datetime_format=True,
                                    index_col=['Date'])
    # remove $ and commas from stock prices
    stock_price_daily['Close/Last'] = stock_price_daily['Close/Last'].astype(str).map(lambda x: x.replace('$', '').replace(',', ''))
    # calculate the percent change in stock price from previous day (daily return)
    stock_returns_daily = stock_price_daily['Close/Last'].astype(float).pct_change()

    # determine returns time interval
    if returns_interval == 'Yearly':
        get_interval_returns(stock_returns_daily, 'Y')
    elif returns_interval == 'Weekly':
        get_interval_returns(stock_returns_daily, 'W')
    elif returns_interval == 'Daily':
        get_interval_returns(stock_returns_daily, 'D')
    else:
        get_interval_returns(stock_returns_daily, 'M')

# -------------
# DISPLAY PLOT
# -------------
plt.legend()
plt.show()



