import pandas as pd
import matplotlib.pyplot as plt

# Load historical stock data
def load_data(symbol, start_date, end_date):
    # Code to load historical stock data using a financial API or a CSV file
    pass

# Moving Average Crossover Strategy
def moving_average_crossover(data, short_window, long_window):
    # Calculate short-term and long-term moving averages
    data['Short_MA'] = data['Close'].rolling(window=short_window).mean()
    data['Long_MA'] = data['Close'].rolling(window=long_window).mean()
    
    # Generate signals
    data['Signal'] = 0
    data.loc[data['Short_MA'] > data['Long_MA'], 'Signal'] = 1  # Buy Signal
    data.loc[data['Short_MA'] < data['Long_MA'], 'Signal'] = -1  # Sell Signal
    
    return data

# Relative Strength Index (RSI) Strategy
def rsi_strategy(data, window):
    # Calculate RSI
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    RS = gain / loss
    RSI = 100 - (100 / (1 + RS))
    
    # Generate signals
    data['RSI'] = RSI
    data['Signal'] = 0
    data.loc[(data['RSI'] < 30) & (data['RSI'].shift(1) > 30), 'Signal'] = 1  # Buy Signal
    data.loc[(data['RSI'] > 70) & (data['RSI'].shift(1) < 70), 'Signal'] = -1  # Sell Signal
    
    return data

# Price Trend Strategy
def price_trend_strategy(data, window):
    # Calculate price trend
    data['Trend'] = data['Close'].rolling(window=window).mean().diff()
    
    # Generate signals
    data['Signal'] = 0
    data.loc[data['Trend'] > 0, 'Signal'] = 1  # Buy Signal
    data.loc[data['Trend'] < 0, 'Signal'] = -1  # Sell Signal
    
    return data

# Main function
def main():
    # Load data
    symbol = 'AAPL'  # Example stock symbol
    start_date = '2020-01-01'
    end_date = '2020-12-31'
    data = load_data(symbol, start_date, end_date)
    
    # Apply trading strategies
    data = moving_average_crossover(data, short_window=50, long_window=200)
    # Alternatively, you can apply other strategies like rsi_strategy() or price_trend_strategy()
    
    # Plot results
    plt.figure(figsize=(10, 5))
    plt.plot(data['Close'], label='Close Price')
    plt.plot(data['Short_MA'], label='50-Day MA')
    plt.plot(data['Long_MA'], label='200-Day MA')
    plt.plot(data[data['Signal'] == 1].index, data['Short_MA'][data['Signal'] == 1], '^', markersize=10, color='g', lw=0, label='Buy Signal')
    plt.plot(data[data['Signal'] == -1].index, data['Short_MA'][data['Signal'] == -1], 'v', markersize=10, color='r', lw=0, label='Sell Signal')
    plt.title('Moving Average Crossover Strategy')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
