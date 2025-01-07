import pandas as pd

# Relative path to the excel file
file_path = 'DAT_XLSX_EURUSD_M1_2018.xlsx'

# Read ecxel file to DataFrame, name the columns
EURUSD = pd.read_excel(file_path, sheet_name= '2018', header=None, names=[
    'Date     Time', 'Open Price', 'High Price', 'Low Price', 'Close Price', 'Volume']) 

# Check the first five rows
print(EURUSD.head())

# Calculate moving average for windows of 5, 10, 15, and 20 days
EURUSD['MA1'] = EURUSD.rolling(window=5)['Close Price'].mean()
EURUSD['MA2'] = EURUSD.rolling(window=10)['Close Price'].mean()
EURUSD['MA3'] = EURUSD.rolling(window=15)['Close Price'].mean()
EURUSD['MA4'] = EURUSD.rolling(window=30)['Close Price'].mean()

print(type(EURUSD['MA4']))
#Check the last five rows. The first five rows of moving average are NaN
print(EURUSD.tail())

# Save the dataframe to the same Excel file
EURUSD.to_excel(file_path, index=False, header=True, sheet_name='2018') 
