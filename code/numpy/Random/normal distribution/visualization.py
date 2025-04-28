from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.normal(loc=10,scale=1,size=1000), hist=True)

plt.show()