import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Download Data


stock = "TCS.NS"
data = yf.download(stock, start="2024-01-01")

close_prices = data['Close'].squeeze()



data['SMA20'] = close_prices.rolling(20).mean()


data['Signal'] = 0
data.loc[close_prices > data['SMA20'], 'Signal'] = 1
data.loc[close_prices < data['SMA20'], 'Signal'] = -1

data.dropna(inplace=True)
close_prices = close_prices.loc[data.index]


initial_capital = 100000
capital = initial_capital
position = 0
shares = 0
entry_price = 0
stop_loss_pct = 0.03   # 3% stop loss

portfolio_values = []
buy_points = []
sell_points = []


# 5. Backtesting Loop

for i in range(len(data)):
    price = close_prices.iloc[i]
    signal = data['Signal'].iloc[i]

    # BUY
    if signal == 1 and position == 0:
        shares = capital // price
        capital -= shares * price
        position = 1
        entry_price = price
        buy_points.append((data.index[i], price))

    # STOP LOSS
    elif position == 1 and price < entry_price * (1 - stop_loss_pct):
        capital += shares * price
        shares = 0
        position = 0
        sell_points.append((data.index[i], price))

    # SELL SIGNAL
    elif signal == -1 and position == 1:
        capital += shares * price
        shares = 0
        position = 0
        sell_points.append((data.index[i], price))

    portfolio_value = capital + shares * price
    portfolio_values.append(portfolio_value)

data['Portfolio'] = portfolio_values


returns = data['Portfolio'].pct_change().dropna()

cumulative_return = (data['Portfolio'].iloc[-1] / initial_capital) - 1
annual_return = returns.mean() * 252
sharpe_ratio = (returns.mean() / returns.std()) * np.sqrt(252)

print("Final Portfolio Value:", round(data['Portfolio'].iloc[-1], 2))
print("Cumulative Return:", round(cumulative_return * 100, 2), "%")
print("Annual Return:", round(annual_return * 100, 2), "%")
print("Sharpe Ratio:", round(sharpe_ratio, 2))



latest_signal = data['Signal'].iloc[-1]

if latest_signal == 1:
    print("Today's Signal: BUY")
elif latest_signal == -1:
    print("Today's Signal: SELL")
else:
    print("Today's Signal: HOLD")



# Price + SMA + Buy/Sell
plt.figure(figsize=(12,5))
plt.plot(close_prices, label='Close Price')
plt.plot(data['SMA20'], label='SMA 20')

for point in buy_points:
    plt.scatter(point[0], point[1], color='green', marker='^', s=100)

for point in sell_points:
    plt.scatter(point[0], point[1], color='red', marker='v', s=100)

plt.title("Price, SMA & Trades")
plt.legend()
plt.xlim(pd.to_datetime("2022-01-01"), pd.to_datetime("2023-01-01"))                  # Zoom price range
plt.show()

# Portfolio Curve
plt.figure(figsize=(12,5))
plt.plot(data['Portfolio'], label='Portfolio Value')
plt.title("Equity Curve")
plt.legend()
plt.show()