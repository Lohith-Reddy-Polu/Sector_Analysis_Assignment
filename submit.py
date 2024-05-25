import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf
import requests
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
#Task1

nifty_indices = {
    'Nifty Auto': '^CNXAUTO',
    'Nifty Bank': '^NSEBANK',
    'Nifty FMCG': '^CNXFMCG',
    'Nifty IT': '^CNXIT',
    'Nifty Media': '^CNXMEDIA',
    'Nifty Metal': '^CNXMETAL',
    'Nifty Realty': '^CNXREALTY',
    'Nifty PSU Bank': '^CNXPSUBANK',
    'Nifty 50': '^NSEI'  # Adding Nifty 50 for comparison
}

variable_indices = {
    'GDP' : 'NY.GDP.MKTP.CD',
    'GDP Per Capita' : 'NY.GDP.PCAP.CD',
    'GDP growth' : 'NY.GDP.MKTP.KD.ZG',
    'UnEmployement' : 'SL.UEM.TOTL.ZS',
    'Inflation' : 'FP.CPI.TOTL.ZG'
}


period = '10y'

nifty_data = {}

for name,ticker in nifty_indices.items():
    print(f'Downloading data : {name}')
    data_name = yf.download(ticker,period = period)
    nifty_data[name] = data_name

econ_data = {}

def fetch_data(indicator):
    url = f"http://api.worldbank.org/v2/country/IN/indicator/{indicator}"
    params = {
        'date': f'{2014}:{2023}',
        'format': 'json',
        'per_page': 1000
    }
    res = requests.get(url=url,params = params).json()
    df = pd.json_normalize(res[1])
    df['date'] = pd.to_datetime(df['date'], format='%Y')
    df.set_index('date', inplace=True)
    return df[['value']]

for key,item in variable_indices.items():
    econ_data[key] = fetch_data(item)
    econ_data[key].to_csv(f"{key}.csv")
    econ_data[key] = pd.read_csv(f'{key}.csv',index_col='date',parse_dates=True)

#Task 2

plt.figure(figsize=(14,7))
for name, df in nifty_data.items():
    plt.plot(df['Close'], label=name)
plt.title('Nifty Sector Indices')
plt.legend()
plt.savefig('Nifty.jpg')
plt.close()


for key,val in econ_data.items():
    plt.plot(val['value'],label = key)
    plt.title(f'{key}')
    plt.legend()
    plt.savefig(f'{key}.jpg')
    plt.close()

# for key in econ_data:
#     econ_data[key] = econ_data[key].resample('M').ffill().reset_index('date')
#     econ_data[key].rename(columns = {'date' : 'Date'},inplace = True)
#     econ_data[key].set_index('Date',inplace = True)

# print(econ_data['GDP'].columns)
# merged_data = pd.DataFrame()
# for key in nifty_data:
#     if merged_data.empty:
#         merged_data = pd.DataFrame(nifty_data[key]['Close'])
#     else:
#         merged_data = merged_data.join(nifty_data[key]['Close'], on='Date', rsuffix=f'{key}')

# for key in econ_data:
#     print(econ_data[key]['value'])
#     merged_data = merged_data.join(econ_data[key]['value'], on='Date', rsuffix=f'{key}')

# merged_data.to_csv('merge.csv')
# print(merged_data)
#Task 3
