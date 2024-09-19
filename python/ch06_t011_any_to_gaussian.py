# define global figure properties used for publication

import matplotlib.pyplot as plt
# define global figure properties used for publication
import matplotlib_inline.backend_inline
import numpy as np
from scipy import stats

matplotlib_inline.backend_inline.set_matplotlib_formats('svg')  # display figures in vector format
plt.rcParams.update({'font.size': 14,  # font size
                     'savefig.dpi': 300,  # output resolution
                     'axes.titlelocation': 'left',  # title location
                     'axes.spines.right': False,  # remove axis bounding box
                     'axes.spines.top': False,  # remove axis bounding box
                     })

X = np.random.normal(0, 5, size=2000) ** 2

X_r = stats.rankdata(X)
a, b = -.999, .999
X_r2 = (X_r - np.min(X_r)) / (np.max(X_r) - np.min(X_r)) * (b - a) + a
X_t = np.arctanh(X_r2)

_, axs = plt.subplots(1, 3, figsize=(10, 4))
axs[0].hist(X, 40, color=(.8, .8, .8), edgecolor='k')
axs[0].set(xlabel='Data value', ylabel='Count')
axs[0].set_title(r'$\bf{A}$)  Raw data hist.')

axs[1].hist(X_t, 40, color=(.8, .8, .8), edgecolor='k')
axs[1].set(xlabel='Data value', ylabel='Count')
axs[1].set_title(r'$\bf{B}$)  Trans. data hist.')

axs[2].plot(X, X_t, 'ko', markersize=8, markerfacecolor=(.8, .8, .8))
axs[2].set(xlabel='Original data', ylabel='Transformed data')
axs[2].set_title(r'$\bf{C}$)  Data comparison')

plt.tight_layout()
plt.savefig('trans_any2gauss.png')
