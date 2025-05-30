import pandas as pd
import talib

# Load stock price data (make sure to replace 'stock_data.csv' with your actual file)
# Expected columns: Date, Open, High, Low, Close, Volume
df = pd.read_csv('data/stock_prices.csv', parse_dates=['Date'])
df.set_index('Date', inplace=True)

# Calculate Simple Moving Average (SMA)
df['SMA_20'] = talib.SMA(df['Close'], timeperiod=20)

# Calculate Relative Strength Index (RSI)
df['RSI_14'] = talib.RSI(df['Close'], timeperiod=14)

# Calculate Moving Average Convergence Divergence (MACD)
macd, macdsignal, macdhist = talib.MACD(df['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
df['MACD'] = macd
df['MACD_Signal'] = macdsignal
df['MACD_Hist'] = macdhist

# Display the last few rows to verify
print(df.tail())

# Save the dataframe with indicators for later use
df.to_csv('data/stock_prices_with_indicators.csv')
