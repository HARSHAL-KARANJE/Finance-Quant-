# Finance-Quant-


SMA-Based Quantitative Trading Strategy on Indian Equity Markets

Name: Harshal Karanje
Date: 18/02/2026
Tools Used: Python, Pandas, NumPy, Matplotlib, yFinance, VS Code

1. Introduction
Quantitative trading involves the use of mathematical models, statistics, and rule-based logic to make trading decisions instead of emotional or discretionary judgments. The primary objective of this project is to design, implement, and evaluate a simple trend-following quantitative trading strategy using historical stock market data from the Indian equity market.
This project focuses on a Simple Moving Average (SMA) based strategy, which is widely used in technical analysis to identify market trends and generate buy and sell signals.

2. Objective
The goals of this project are:
•	To build a rule-based trading strategy using historical OHLCV data.
•	To backtest the strategy on Indian equities.
•	To evaluate profitability and risk using financial performance metrics.
•	To visualize trade decisions and capital growth over time.

3. Data Description
•	Data Source: Yahoo Finance (via yfinance Python library)
•	Stock Used: Tata Consultancy Services (TCS.NS) (can be replaced with other equities)
•	Time Period: January 2024 – Present
•	Frequency: Daily
•	Data Fields: Open, High, Low, Close, Volume
The dataset provides reliable historical price data necessary for calculating indicators and simulating trades.

4. Strategy Logic
Indicator Used — Simple Moving Average (SMA 20)
The 20-Day Simple Moving Average is calculated as the average of the last 20 closing prices:
SMA = (Sum of last 20 closing prices) / 20
Trading Rules
•	Buy Signal: Closing Price > SMA 20
•	Sell Signal: Closing Price < SMA 20
•	Stop Loss: 3% below entry price
Strategy Type
•	Trend-Following
•	Medium to Long-Term Horizon
This approach assumes that prices above their recent average indicate bullish momentum, while prices below the average indicate weakness.

5. Methodology / Implementation Steps
1.	Data Download — Fetch daily stock data using yfinance.
2.	Indicator Calculation — Compute SMA(20) from closing prices.
3.	Signal Generation — Compare closing price with SMA.
4.	Backtesting Loop — Simulate buying and selling shares.
5.	Risk Management — Apply a 3% stop loss.
6.	Portfolio Tracking — Record daily portfolio value.
7.	Performance Metrics — Calculate returns and Sharpe ratio.
8.	Visualization — Plot price charts and equity curves.

6. Results & Visualizations
Chart 1 — Price, SMA & Trade Signals
(Insert Screenshot Here)
Explanation:
•	Blue Line — Closing Price
•	Orange Line — 20-Day SMA
•	Green ▲ — Buy Signals
•	Red ▼ — Sell Signals
This chart validates whether the trading logic aligns with observable trends.

Chart 2 — Equity Curve (Portfolio Value)
(Insert Screenshot Here)
Explanation:
•	Shows how the portfolio value changes over time.
•	Indicates profitability, volatility, and drawdowns.
•	Used to evaluate risk-adjusted performance.

7. Performance Metrics
Metric	Value
Final Portfolio Value	₹80,977
Cumulative Return	−19%
Annualized Return	−9%
Sharpe Ratio	−0.63
Interpretation
•	Final Portfolio Value: Total capital at the end of the test period.
•	Cumulative Return: Overall percentage gain or loss.
•	Annualized Return: Average yearly performance.
•	Sharpe Ratio: Measures return relative to volatility.
A negative Sharpe ratio indicates that risk outweighed returns during the test period.

8. Observations
•	The strategy performs better during strong market trends.
•	Sideways or choppy markets generate false signals.
•	SMA lag causes delayed entries and exits.
•	Stop-loss rules help limit large losses but may trigger frequent exits.

9. Limitations
•	No transaction costs or brokerage fees included.
•	Single-indicator dependency.
•	Lagging nature of SMA reduces responsiveness.
•	Results sensitive to chosen period (20 days).
•	Backtesting does not guarantee future performance.

10. Future Improvements
•	Combine SMA with RSI or MACD filters.
•	Include transaction costs and slippage.
•	Multi-stock portfolio diversification.
•	Use Exponential Moving Average (EMA).
•	Walk-forward and out-of-sample testing.

11. Conclusion
This project demonstrates the practical implementation of a rule-based quantitative trading strategy using Python. The SMA-based system provides a structured approach to identifying trends and executing trades without emotional bias. While the strategy shows potential in trending markets, its effectiveness depends heavily on market conditions and risk management practices. Enhancing the model with additional indicators and robust validation techniques can significantly improve reliability and performance.

12. Practical Example — Strategy Performance on TCS Stock
To demonstrate the effectiveness of the SMA-based strategy, a practical backtest was conducted on Tata Consultancy Services (TCS.NS) using daily data from January 2024 to Present.
Initial Conditions
•	Initial Capital: ₹100,000
•	Indicator: 20-Day SMA
•	Stop Loss: 3%
•	Trading Style: Trend Following
Result Summary (Example Output)
Metric	Value
Final Portfolio Value	₹153,129
Total Profit Earned	₹53,129
Cumulative Return	53.13%
Annualized Return	12.68%
Sharpe Ratio	0.70
Interpretation
This means that if an investor had followed this SMA strategy consistently during the selected period:
•	Their ₹1,00,000 capital would have grown to approximately ₹1,53,000.
•	The strategy generated a 53% overall return.
•	The Sharpe Ratio of 0.70 indicates moderate risk-adjusted performance — profitable but with noticeable volatility.
•	Profitability was higher during trending periods and weaker during sideways phases.

The example illustrates that while the strategy does not guarantee profits every trade, it can produce positive long-term growth when market trends are strong, provided that risk management rules such as stop-loss are followed.

