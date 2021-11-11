import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime


df = pd.read_csv("3131.csv")


def getYearFromDate(date):
    '''Input: row number
    return: year of date of that row in dataframe'''

    return datetime.strptime(date, '%Y-%m-%d').year


def getDateObjectFromRow(rowIndex):
    '''Input: row number
    return: datetime object of date of that row in dataframe'''

    return datetime.strptime(df.iloc[rowIndex]['datetime'], '%Y-%m-%d')


rowIndex = sorted(set([getYearFromDate(date) for date in df['datetime']]))
colIndex = ['Jan', 'Feb', 'Mar', 'Apr', 'May',
            'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

df_percent = pd.DataFrame(
    columns=colIndex, index=rowIndex, dtype=float).fillna(0)


month_open_index = 0  # 1st data is month open data

for i in range(df.shape[0]):

    current_date = getDateObjectFromRow(i)
    month_open_date = getDateObjectFromRow(month_open_index)

    # new month has started, i-1 was month close, for last data point it is the last date
    if (current_date.month != month_open_date.month or i == df.shape[0]-1):
        month_closing_price = df.loc[i]['close'] if i == df.shape[0] - \
            1 else df.loc[i-1]['close']

        month_open_price = df.loc[month_open_index]['open']
        month_percent = (month_closing_price -
                         month_open_price)/month_open_price * 100

        df_percent.loc[month_open_date.year][month_open_date.strftime(
            '%b')] = month_percent

        month_open_index = i  # this is new month start


plt.figure(figsize=(16, 16))
heatmap_plot = sns.heatmap(data=df_percent, annot=True, cmap='RdYlGn')
plt.savefig("MonthlyPercent")
