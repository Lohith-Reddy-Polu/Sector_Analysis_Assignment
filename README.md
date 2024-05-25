# Sector_Analysis_Assignment

I only did Task1 and Task2,got struck in Task3.

In Task1,I used `yfinance` library to fetch data for various sectoral indices.
I then sent request to `http://api.worldbank.org/v2/country/IN/indicator/{indicator}` to get data for each economic variable.
Indicators I obtained are : 1)GDP 2)GDP Per Capita 3)GDP growth 4)UnEmployement 5)Inflation

In Task2,I generated a lineplot,showing the variation of all sectoral indices over time,it's stored in `Nifty.jpg`.
And I generated plots for each economic variable over the past 10 years,the plots are generated in their `{name_of_variable}.jpg`.
(These plots matches with the plots present in the resources)
