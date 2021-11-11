from datetime import datetime, timedelta
import sys

wednesday = 3


def inputFormatCheck(input_date):
    try:
        year, month, day = input_date.split('-')
        if (len(year) != 4 or len(month) != 2 or len(day) != 2):
            return False
        return True
    except:
        return False


print("Please enter date in YYYY-MM-DD format")
input_date = input()

if (inputFormatCheck(input_date) == False):
    print("Please enter correct date format and try again")
    sys.exit(0)

input_date_object = datetime.strptime(input_date, '%Y-%m-%d')

# to iterate through the entire days of the inputted month
current_date = datetime(input_date_object.year, input_date_object.month, 1)
last_wednesday = current_date

while(current_date.month == input_date_object.month):
    if (current_date.isoweekday() == wednesday):
        last_wednesday = current_date
    current_date = current_date + timedelta(days=1)

print(last_wednesday)
