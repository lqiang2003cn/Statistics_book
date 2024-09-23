# import libraries and define global settings
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

_, axs = plt.subplots(2, 2, figsize=(12, 6))

# panel A: unexpected range
x = np.concatenate((np.random.randn(20), np.random.randn(80) * 30), axis=0)
axs[0, 0].plot(x, 'ks', markersize=10, markerfacecolor=(.7, .7, .7), alpha=.8)
axs[0, 0].set(xlabel='Data index', xticks=[], yticks=[], ylabel='Data value')
axs[0, 0].set_title(r'$\bf{A}$)  Unexpected data range')

# panel B: distribution shape
x = np.concatenate((5 + np.random.randn(150), np.exp(1 + np.random.randn(150))), axis=0)
axs[0, 1].hist(x, bins='fd', edgecolor='k', facecolor=(.7, .7, .7))
axs[0, 1].set(xlabel='Data value', xticks=[], yticks=[], ylabel='Count')
axs[0, 1].set_title(r'$\bf{B}$)  Nonstandard distribution')

# panel C: mixed datasets
x = np.concatenate((4 + np.random.randn(150), np.random.randn(150) - 4), axis=0)
axs[1, 0].hist(x, bins=50, edgecolor='k', facecolor=(.7, .7, .7))
axs[1, 0].set(xlabel='Data value', xticks=[], yticks=[], ylabel='Count')
axs[1, 0].set_title(r'$\bf{C}$)  Mixed dataset')

# panel D: outliers
x = np.random.randn(150)
x[60] = 10
x[84] = 14
axs[1, 1].plot(x, 'ks', markersize=10, markerfacecolor=(.7, .7, .7), alpha=.8)
axs[1, 1].set(xlabel='Data index', xticks=[], yticks=[], ylabel='Data value')
axs[1, 1].set_title(r'$\bf{B}$)  Outliers')

# export
plt.tight_layout()
plt.savefig('dataQC_qualInspection.png')
