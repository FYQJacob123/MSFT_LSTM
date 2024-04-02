import yfinance as yf
from matplotlib import pyplot as plt
import webbrowser
import time
from datetime import datetime
import os
def fetch_and_save_msft_data():
    # Load the MSFT Stock closing prices data from Yahoo Finance for the period 2018-01-01 to the latest date
    msft = yf.Ticker("MSFT")
    hist = msft.history(period="max")
    hist = hist[hist.index >= '2018-01-01']
    hist = hist[['Close']]
    hist = hist.rename(columns={'Close': 'MSFT'})
    hist = hist.dropna() 

    # Save the data to a CSV file
    hist.to_csv('MSFT.csv')

    # Plot the data
    plt.figure(figsize=(10, 5))
    plt.plot(hist)
    plt.title('MSFT Stock Price')
    plt.ylabel('Price')
    plt.grid()
    plt.savefig('MSFT.png')

while True:
    fetch_and_save_msft_data()
    print(f"Data updated at {datetime.now()}")
    time.sleep(60)  # Wait for 60 seconds before the next update
