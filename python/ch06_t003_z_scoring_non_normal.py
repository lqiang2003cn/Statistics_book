# define global figure properties used for publication

import matplotlib.pyplot as plt
# define global figure properties used for publication
import matplotlib_inline.backend_inline
import numpy as np

matplotlib_inline.backend_inline.set_matplotlib_formats('svg')  # display figures in vector format
plt.rcParams.update({'font.size': 14,  # font size
                     'savefig.dpi': 300,  # output resolution
                     'axes.titlelocation': 'left',  # title location
                     'axes.spines.right': False,  # remove axis bounding box
                     'axes.spines.top': False,  # remove axis bounding box
                     })

N = 5000
X = (1 + np.random.exponential(size=N)) * 10
Xz = (X - np.mean(X)) / np.std(X, ddof=1)

_, axs = plt.subplots(2, 1, figsize=(8, 7))
axs[0].hist(X, bins='fd', color=(.9, .9, .9), edgecolor='k')
axs[0].axvline(np.mean(X), color='k', linestyle='--')
axs[0].set(xlabel='Raw data value', ylabel='Count', xlim=[8, 80])
axs[0].set_title(r'$\bf{A}$)  Histogram of raw data')

axs[1].hist(Xz, bins='fd', color=(.9, .9, .9), edgecolor='k')
axs[1].axvline(np.mean(Xz), color='k', linestyle='--')
axs[1].set(xlabel='Z-transformed data value', ylabel='Count', xlim=[-1.2, 5])
axs[1].set_title(r'$\bf{B}$)  Histogram of z-transformed data')

plt.tight_layout()
plt.savefig('trans_zscore_positive.png')
