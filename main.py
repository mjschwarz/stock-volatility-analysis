import math
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import datetime as dt


# -----------------------
# CONSTANTS AND VARIABLES
# -----------------------
TRADING_DAYS_YEAR = 252
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 4.83

SP_500 = 'VOO'

tickers = input('Enter the STOCK TICKER(S) separated by spaces: ').upper().split()
print()

START = dt.datetime(int(input('Enter the STARTING YEAR: ')),
                    int(input('Enter the STARTING DAY: ')),
                    int(input('Enter the STARTING MONTH: ')))
print()

END = dt.datetime(int(input('Enter the ENDING YEAR: ')),
                  int(input('Enter the ENDING DAY: ')),
                  int(input('Enter the ENDING MONTH: ')))
print()


# -----------
# PLOT SETUP
# -----------
plt.style.use('seaborn-darkgrid')
plt.title('Stock Volatility vs. S&P 500')
plt.ylabel('Volatility')
plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1, decimals=None, symbol='%', is_latex=False))


# ---------------
# HELPER METHODS
# ---------------
def calc_volatility(d_pct_change, tkr):
    """
    Calculates and prints to the console the volatility of a stock
    at annual, monthly, weekly, and daily intervals.
    :param d_pct_change: daily percentage change in adjusted closing price
    :param tkr: ticker
    """
    annual_volatility = d_pct_change.std() * math.sqrt(TRADING_DAYS_YEAR)
    monthly_volatility = d_pct_change.std() * math.sqrt(TRADING_DAYS_MONTH)
    weekly_volatility = d_pct_change.std() * math.sqrt(TRADING_DAYS_WEEK)
    daily_volatility = d_pct_change.std()

    if tkr == SP_500:
        print('S&P 500 Volatility')
    else:
        print(f'{tkr} Volatility')
    print(f'Annual: {annual_volatility * 100:.2f}%')
    print(f'Monthly: {monthly_volatility * 100:.2f}%')
    print(f'Weekly: {weekly_volatility * 100:.2f}%')
    print(f'Daily: {daily_volatility * 100:.2f}%')
    print()


def get_data(tkr):
    """
    Gets the adjusted closing price data of a stock.
    Data retrieved from Yahoo Finance.
    :param tkr: ticker
    :return: daily adjusted closing price
    """
    daily_adj_close = web.DataReader(tkr, 'yahoo', start=START, end=END)['Adj Close']
    return daily_adj_close


def calc_pct_change(d_adj_close):
    """
    Calculates the daily percentage change in adjusted closing price.
    :param d_adj_close: daily adjusted closing price
    :return: daily percentage change in adjusted closing price
    """
    daily_pct_change = d_adj_close.pct_change()
    return daily_pct_change


def plot_data(d_pct_change, tkr):
    """
    Plots the daily volatility data from the parametrized ticker.
    :param d_pct_change: daily volatility data
    :param tkr: ticker
    """
    if tkr == SP_500:
        d_pct_change.plot(label='S&P 500', zorder=10)
    else:
        d_pct_change.plot(label=tkr, alpha=0.8)


# --------------------------------
# DATA COLLECTION AND MANIPULATION
# --------------------------------
SP_500_data = calc_pct_change(get_data(SP_500))
plot_data(SP_500_data, SP_500)
calc_volatility(SP_500_data, SP_500)

for ticker in tickers:
    ticker_data = calc_pct_change(get_data(ticker))
    plot_data(ticker_data, ticker)
    calc_volatility(ticker_data, ticker)


# -------------
# DISPLAY PLOT
# -------------
plt.legend()
plt.show()
