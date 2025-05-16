import pandas as pd

a = {"day1": 420, "day2": 30, "day3": 100}
x = pd.Series(a)
print(x["day2"])

# 30