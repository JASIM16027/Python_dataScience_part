import pandas as pd

data = pd.read_csv('employee_inf.csv')

# removing null values to avoid errors
data.dropna(inplace=True)

percentile = [.20, .40, .60, .80]

# list of data type to include
include = ['object', 'float', 'int']
descr = data['Name'].describe()

print(descr)
# calling describe method
desc = data.describe(percentiles=percentile, include= include)
print(desc)

