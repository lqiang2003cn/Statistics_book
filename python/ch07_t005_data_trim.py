# import libraries and define global settings
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

N = 74
data = np.random.randn(N) ** 3

# find largest and smallest values
k = 2
sortidx = np.argsort(data)
minvals = sortidx[:k]
maxvals = sortidx[-k:]

_, axs = plt.subplots(2, 1, figsize=(8, 6))
axs[0].plot(data, 'ks', markersize=10, markerfacecolor=(.9, .9, .9))
axs[0].plot(minvals, data[minvals], 'kx', markersize=10, markeredgewidth=2)
axs[0].plot(maxvals, data[maxvals], 'kx', markersize=10, markeredgewidth=2)
axs[0].set_title(r'$\bf{A}$)  Data with k-extreme points trimmed')

# create a Gaussian probability curve for the panel B
x = np.linspace(-4, 4, 401)
gpdf = stats.norm.pdf(x)

# the find the indices of the 2.5% and 97.5%
lbndi = np.argmin(np.abs(x - stats.norm.ppf(.025)))  # lbndi = Lower BouND Index
ubndi = np.argmin(np.abs(x - stats.norm.ppf(1 - .025)))

# plot the probability function and the vertical lines
axs[1].plot(x, gpdf, 'k', linewidth=2)
axs[1].axvline(x[lbndi], color=(.5, .5, .5), linewidth=.5, linestyle='--')
axs[1].axvline(x[ubndi], color=(.5, .5, .5), linewidth=.5, linestyle='--')
axs[1].set(xlim=x[[0, -1]], ylim=[0, .42])
axs[1].set_title(r'$\bf{B}$)  Histogram showing trimmed areas')

# now create patches for the rejected area
axs[1].fill_between(x[:lbndi + 1], gpdf[:lbndi + 1], color='k', alpha=.4)
axs[1].fill_between(x[ubndi:], gpdf[ubndi:], color='k', alpha=.4)

# and save
plt.tight_layout()
plt.savefig('dataQC_trimming.png')
