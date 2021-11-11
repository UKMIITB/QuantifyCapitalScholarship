import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv("3131.csv")

df['datetime'] = pd.to_datetime(df['datetime'], format='%Y-%m-%d')
df = df.sort_values('datetime')

df['year'] = df.apply(lambda x: x['datetime'].year, axis=1)
df['month'] = df.apply(lambda x: x['datetime'].month, axis=1)

df_first = df.groupby(['year', 'month']).agg(
    'first').reset_index()[['year', 'month', 'open']]

df_last = df.groupby(['year', 'month']).agg(
    'last').reset_index()[['year', 'month', 'close']]

df_first.rename(columns={'open': 'month_open_price'}, inplace=True)
df_last.rename(columns={'close': 'month_closing_price'}, inplace=True)

df_merged = df_first.merge(df_last, on=['year', 'month'])

df_merged['return'] = df_merged.apply(lambda x: (
    x['month_closing_price'] - x['month_open_price'])*100/x['month_open_price'], axis=1)

df_merged = df_merged[['year', 'month', 'return']]

final_df = df_merged.pivot_table(index='year', columns='month')

final_df.columns = final_df.columns.droplevel()

final_df.rename(columns={1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May',
                         6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}, inplace=True)

plt.figure(figsize=(16, 16))
heatmap_plot = sns.heatmap(data=final_df, annot=True, cmap='RdYlGn')
plt.savefig("MonthlyPercent")
