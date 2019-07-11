import pandas_datareader.data as pdr
import matplotlib.pyplot as plt 
import datetime
import matplotlib.dates as mdates

stocks = ['VTI','VOO','IAU','GLD']
year = 2015

#end = datetime.datetime(2018,12,31)
#year = datetime.timedelta(days=200)
#start = datetime.datetime.today() - year
start = datetime.datetime(year,1,1)
end = datetime.datetime(year,12,31)

#def total_return(prices):
#    return prices.iloc[-1] / prices.iloc[0] - 1

for i in range(len(stocks)):
    df = pdr.get_data_yahoo(stocks[i], start=start, end=end)['Adj Close']
    #tr = df.apply(total_return)
    tr = df.iloc[-1] / df.iloc[0] -1
    #out = tr.iloc[0].astype(float)
    print('%s = %.1f%%' %(stocks[i], (tr * 100)))
#df.plot()
#plt.show() 