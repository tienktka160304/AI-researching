import pandas as pd

data = {
    "calories" : [420, 380, 200],
    "duration" : [50,40,45]
}

print(pd.DataFrame(data))

#    calories  duration
# 0       420        50
# 1       380        40
# 2       200        45