import pandas as pd

#specify the encoding while reading
x = pd.read_csv('data.csv', encoding='utf-8') 

print(x.to_string()) #continuous no decrete
#      Duration  Pulse  Maxpulse  Calories
# 0          60    110       130     409.1
# 1          60    117       145     479.0
# 2          60    103       135     340.0
# 3          45    109       175     282.4
# 4          45    117       148     406.0
# 5          60    102       127     300.5
# 6          60    110       136     374.0
# 7          45    104       134     253.3
...
# 168        75    125       150     330.4

print(x)
#      Duration  Pulse  Maxpulse  Calories
# 0          60    110       130     409.1
# 1          60    117       145     479.0
# 2          60    103       135     340.0
# 3          45    109       175     282.4
# 4          45    117       148     406.0
# ..        ...    ...       ...       ...
# 164        60    105       140     290.8
# 165        60    110       145     300.4
# 166        60    115       145     310.2
# 167        75    120       150     320.4
# 168        75    125       150     330.4

# [169 rows x 4 columns]