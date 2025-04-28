import pandas

my_dataset = {
    'cars' : ["BMW", "Volvo"],
    'passings': [3, 7]
}

print(pandas.DataFrame(my_dataset))

#     cars  passings
# 0    BMW         3
# 1  Volvo         7