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

# number of samples
nSamples = 50

# histogram resolution
k = 30
edges = np.linspace(-3, 14, 31)
xx = (edges[:-1] + edges[1:]) / 2

# initialize output matrices
meenz = np.zeros(nSamples)  # sample averages
allYYs = np.zeros(k)  # average of histograms

_, axs = plt.subplots(2, 1, figsize=(4, 6))

# loop over samples
for i in range(nSamples):
    # generate random data from an exGaussian distribution
    randomX = stats.exponnorm.rvs(np.random.uniform(low=.1, high=5), size=2000)

    # get its histogram and normalize
    yy, _ = np.histogram(randomX, bins=edges)
    yy = yy / np.sum(yy)

    # average the distributions
    allYYs += yy

    # store the average of the distribution
    meenz[i] = np.mean(randomX)

    # plot the line
    rc = np.random.uniform(low=.4, high=.8)  # random color
    axs[0].plot(xx, yy, linewidth=.5, color=(rc, rc, rc))
    axs[0].plot(meenz[i], yy[np.argmin(np.abs(xx - meenz[i]))], 'k*', linewidth=.2,
                markerfacecolor=(rc, rc, rc), markersize=12)

# some plotting adjustments
axs[0].set(xlim=xx[[0, -1]], ylabel='Probability', yticks=[])
axs[0].set_title(r'$\bf{B}$)  Data distributions')

## the distribution of sample means
axs[1].hist(meenz, 20, facecolor=(.7, .7, .7), edgecolor='k')
axs[1].plot(xx, allYYs / np.max(allYYs) * 5, 'k', zorder=-10)
axs[1].set(xlim=xx[[0, -1]], xlabel='Data value', ylabel='Count', yticks=[])
axs[1].set_title(r'$\bf{C}$)  Means distribution')

# output
plt.tight_layout()
plt.savefig('sample_distOfExGausMeans.png')
