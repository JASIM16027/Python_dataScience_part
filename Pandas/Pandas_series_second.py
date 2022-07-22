import numpy as np
import pandas as pd

# making DataFrame
data = pd.read_csv('employee_inf.csv')
# by Default take 5 rows
data_top1 = data.head(10)
print(data_top1)
# creating series
series = data['Name']

data_top = series.head(n=10)
print(data_top)


