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


def minmaxScaling(x):
    # compute min/max values
    minx = np.min(x)
    maxx = np.max(x)

    # transformation
    xScaled = (x - minx) / (maxx - minx)

    # output
    return xScaled


# Note: I wrote the function over multiple lines for clarity; you could reduce it to one line!
# %%
## create some data

N = 42
data = np.log(np.random.rand(N)) * 234 + 934

# now min-max scale
dataS = minmaxScaling(data)

# now plot
fig, ax = plt.subplots(1, 3, figsize=(10, 4))
randomXoffsets = 1 + np.random.randn(N) / 20
ax[0].plot(randomXoffsets, data, 'ks', markerfacecolor='w')
ax[0].set(xlim=[0, 2], xticks=[], ylabel='Original data scale')
ax[0].set_title(r'$\bf{A}$)  Original data')

ax[1].plot(randomXoffsets, dataS, 'ks', markerfacecolor='w')
ax[1].set(xlim=[0, 2], xticks=[], ylabel='Unity-normed data scale')
ax[1].set_title(r'$\bf{B}$)  Scaled data')

ax[2].plot(data, dataS, 'ks', markerfacecolor='w')
ax[2].set(xlabel='Original values', ylabel='Scaled values')
ax[2].set_title(r'$\bf{C}$)  Scatter plot')

plt.tight_layout()
plt.savefig('trans_minmax.png')
