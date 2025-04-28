import pandas as pf

data = {
    "calories" : [32,43,56],
    "name" : [32,45,76]
}

x = pf.DataFrame(data, index = ["day1","day2","day3"])

print(x)

#       calories  name
# day1        32    32
# day2        43    45
# day3        56    76

print(x.loc["day2"])
# calories    43
# name        45
# Name: day2, dtype: int64