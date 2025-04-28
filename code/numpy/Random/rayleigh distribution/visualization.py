from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns 

sns.distplot(random.rayleigh(size=100),hist=False)

plt.show()