from datetime import datetime, timedelta
import pandas as pd

df = pd.read_csv("3131.csv")
df_expiry = pd.DataFrame().reindex(columns=df.columns)

thursday = 4  # 4th day of the week


def getDateObjectFromRow(rowIndex):
    '''Input: row number
    return: datetime object of date of that row in dataframe'''

    return datetime.strptime(df.iloc[rowIndex]['datetime'], '%Y-%m-%d')


row_index = 0  # to iterate through all rows in dataframe

# this will iterate day by day from start date
current_date = getDateObjectFromRow(0)


# to ensure we iterate through all rows of dataframe
while (row_index < df.shape[0]):

    if (current_date.isoweekday() == thursday):
        # whatever is the current date in dataframe is the actual expiry

        if (getDateObjectFromRow(row_index).isoweekday() == thursday):
            df_expiry = df_expiry.append(df.iloc[row_index], ignore_index=True)
        else:  # the previous date in actual data is the real expiry
            df_expiry = df_expiry.append(
                df.iloc[row_index - 1], ignore_index=True)

    if (current_date == getDateObjectFromRow(row_index)):  # move to next row data point
        row_index = row_index + 1

    current_date = current_date + timedelta(days=1)  # move to next day

df_expiry = df_expiry.drop_duplicates(subset='datetime', keep="last")
df_expiry.to_csv("expiryData.csv", encoding='utf-8', index=False)
