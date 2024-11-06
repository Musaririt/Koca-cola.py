import yfinance as yf
import plotly.graph_objects as go

# Define the ticker symbol for Coca-Cola
ticker_symbol = "KO"

# Get the stock data
stock_data = yf.download(ticker_symbol)

# Create a candlestick chart
fig = go.Figure(data=[go.Candlestick(x=stock_data.index,
                                    open=stock_data['Open'],
                                    high=stock_data['High'],
                                    low=stock_data['Low'],
                                    close=stock_data['Close'])])

# Set the title and axis labels
fig.update_layout(title_text="Coca-Cola Stock Prices",
                  yaxis_title="Price (USD)")

# Display the chart
fig.show()
