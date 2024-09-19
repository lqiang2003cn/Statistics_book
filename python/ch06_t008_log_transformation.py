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

# generate data from power-law distribution
X = np.random.normal(0, 5, size=2000) ** 2
Xlog = np.log(X)

_, axs = plt.subplots(2, 2, figsize=(10, 7))

# scatter plots
axs[0, 0].plot(X, 'ko', markerfacecolor='w')
axs[0, 0].set(xlabel='Data index', ylabel='Data value')
axs[0, 0].set_title(r'$\bf{A}$)  Raw data')

axs[0, 1].plot(Xlog, 'ko', markerfacecolor='w')
axs[0, 1].set(xlabel='Data index', ylabel='ln(data)')
axs[0, 1].set_title(r'$\bf{B}$)  Transformed data')

# histograms
axs[1, 0].hist(X, bins='fd', color=(.9, .9, .9), edgecolor='k')
axs[1, 0].set_title(r'$\bf{C}$)  Histogram of raw data')

axs[1, 1].hist(Xlog, bins='fd', color=(.9, .9, .9), edgecolor='k')
axs[1, 1].set_title(r'$\bf{D}$)  Histogram of ln(data)')

plt.tight_layout()
plt.savefig('trans_logdata_example.png')
