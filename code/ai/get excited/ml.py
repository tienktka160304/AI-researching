import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('social_network_ads.csv', encoding='utf-8')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

#display the dataset
print(dataset)

#plot the dataset

from matplotlib.colors import ListedColormap
from matplotlib.axes._axes import _log as matplotlib_axes_logger
matplotlib_axes_logger.setLevel('ERROR')
X_set, y_set = X, y
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 10, stop = X_set[:, 0].max() + 10, step = 0.25), np.arange(start = X_set[:, 1].min() - 1000, stop = X_set[:, 1].max() + 1000, step = 0.25))

plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())

for i, j in enumerate(np.unique(y_set)):
    color = ListedColormap(('salmon', 'dodgerblue'))
    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1], c = , label = j)
    
plt.title("Previous Campaign Data")
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()