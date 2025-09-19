import pandas as pd
import numpy as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Fetch

ticker = 'AAPL'
start_date = '2020-01-01'
end_date = '2024-01-01'

data = yf.download(ticker, start = start_date, end = end_date)

print(data.head())
