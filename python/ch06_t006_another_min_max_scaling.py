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


def minmaxScaling(x):
    # compute min/max values
    minx = np.min(x)
    maxx = np.max(x)

    # transformation
    xScaled = (x - minx) / (maxx - minx)

    # output
    return xScaled


# generate a Laplace distribution
x1 = np.exp(-np.abs(3 * np.random.randn(40)))
x2 = np.exp(-np.abs(3 * np.random.randn(40)))
x = (x1 - x2) * 42 - 13

# minmax scale
xm = minmaxScaling(x)

_, axs = plt.subplots(2, 1, figsize=(4, 8))

axs[0].hist(x, bins='fd', color=(.9, .9, .9), edgecolor='k')
axs[0].set(yticks=[], ylabel='Count (a.u.)', xlabel='Raw data values')
axs[0].set_title(r'$\bf{A}$)  Histogram of raw data')

axs[1].hist(xm, bins='fd', color=(.9, .9, .9), edgecolor='k')
axs[1].set(yticks=[], ylabel='Count (a.u.)', xlabel='Minmax-scaled values')
axs[1].set_title(r'$\bf{B}$)  Hist. of transformed data')

plt.tight_layout()
plt.savefig('trans_minmax_exampleHist.png')
