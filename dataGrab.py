import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd #framework pentru analizarea datelor
import pandas_datareader as web #framework pentru aducere de date (bazat pe API de la Yahoo)

style.use('ggplot')
#start = dt.datetime(2001,1,1)
#end = dt.datetime(2017,12, 31)

#df = web.DataReader("TSLA", 'morningstar', start, end)
#print(df.head())
#df.to_csv('tsla.csv')
df = pd.read_csv('tesla.csv', parse_dates = True, index_col=0)
print(df.head())
df.plot()
plt.show()
