import pandas as pd
import numpy as np


data = pd.read_csv('student_inf.csv', index_col='Name')
print(data, '\n\n\n')
first = data.loc['Jasim uddin']
second = data.loc['Md. Rakib hasan']

print(first, '\n\n\n', second)
