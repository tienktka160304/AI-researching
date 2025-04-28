import pandas as pd
import numpy as np

df = pd.read_csv('testfile.csv')

print(df.to_string())

arr = np.array([1, 2, 3,4 ,5 ,34, 3,2,2])

x = np.where(arr == 2)

print(x)
