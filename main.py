import pandas_datareader.data as pdr
import matplotlib.pyplot as plt 
import datetime
import statistics

stocks = ['VOO','VB','IAU','BND','AMD']
start_year = 2005
end_year = 2018
#column = 'Close'
column = 'Adj Close'

#end = datetime.datetime(2018,12,31)
#year = datetime.timedelta(days=200)
#start = datetime.datetime.today() - year
start = datetime.datetime(start_year,1,1)
end = datetime.datetime(end_year,12,31)

def total_return(prices):
    return prices.iloc[-1] / prices.iloc[0] - 1

list = []

print('Column type = %s' % column)
for i in range(len(stocks)):
    df = pdr.get_data_yahoo(stocks[i], start=start, end=end)[column]
    #tr = df.apply(total_return)
    tr = df.iloc[-1] / df.iloc[0] -1
    avg_tr = tr / (end_year - start_year +1)
    list.append(avg_tr)
    std = df.std()
    #tr = tr.iloc[0].astype(float)
    print('%s (%d ~ %d)= %.1f%%, AVG(Y)= %.1f%%, STD= %.1f' 
    %(stocks[i], start_year, end_year,(tr * 100), (avg_tr * 100), std ))
print('===================================')
print('Total AVG(Y) in %d targets = %.1f%% ' %(len(list),(statistics.mean(list)*100)))

#df.plot()
#plt.show()