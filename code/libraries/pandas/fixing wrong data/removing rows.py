import pandas as pd

df = pd.read_csv('data.csv')

for x in df.index:
    if df.loc[x, 'Duration'] > 50:
        df.drop(x,inplace=True)
        
print(df.to_string())

#     Duration          Date  Pulse  Maxpulse  Calories
# 3         45  '2020/12/04'    109       175     282.4     
# 4         45  '2020/12/05'    117       148     406.0     
# 8         30  '2020/12/09'    109       133     195.1     
# 18        45  '2020/12/18'     90       112       NaN     
# 20        45  '2020/12/20'     97       125     243.0     
# 22        45           NaN    100       119     282.0     
# 24        45  '2020/12/24'    105       132     246.0  