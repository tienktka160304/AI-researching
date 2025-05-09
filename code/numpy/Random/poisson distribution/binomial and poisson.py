from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns 

sns.distplot(random.binomial(n=1000,p=0.1,size=1000),hist=False,label='binomial')
sns.distplot(random.poisson(lam=10,size=1000),hist=False, label='poisson')

plt.legend()
plt.show()