from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns 

sns.distplot(random.pareto(a=2,size=1000), hist=True,kde=True)

plt.show()