import pandas as pd

data = {
    "name" : ["tien", "hai","em"],
    "tuoi" : ["15","23", "33"]
}

x = pd.DataFrame(data)

print(x.loc[1] +" "+ x.loc[0])
# name    hai tien
# tuoi       23 15
# dtype: object

print(x.loc[[0,1]] )   
#    name tuoi
# 0  tien   15
# 1   hai   23