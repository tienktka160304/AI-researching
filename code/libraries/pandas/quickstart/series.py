import pandas as pd

a = [1,7,2,3]

x = pd.Series(a, index = ['z','c','a','b'])
print(x['c'])

# 7