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

# create some raw data
N = 10  # sample size
data = np.exp(np.random.randn(N) / 2) + 5
data[-1] = np.max(data) + 2  # impose an outlier (at the end for convenience)
xvals = np.arange(N)

dataZ1 = (data - np.mean(data)) / np.std(data, ddof=1)
dataZ2 = (data[:-1] - np.mean(data[:-1])) / np.std(data[:-1], ddof=1)

_, axs = plt.subplots(1, 2, figsize=(10, 4))
axs[0].plot(xvals, data, 'ks', markersize=10, markerfacecolor=(.7, .7, .7))
axs[0].set(xticks=[], xlabel='Data index', ylabel='Raw data value')
axs[0].set_title(r'$\bf{A}$)  Raw data')

axs[1].plot(xvals, dataZ1, 'ks', markersize=10, markerfacecolor=(.7, .7, .7), label='Z with outlier')
axs[1].plot(xvals[:-1], dataZ2, 'ko', markersize=10, markerfacecolor=(.5, .5, .5), label='Z without outlier')
axs[1].set(xticks=[], xlabel='Data index', ylabel='Transformed data value')
axs[1].legend()
axs[1].set_title(r'$\bf{B}$)  Z-transformed data')

# draw lines connection pre/post-removal values
for d, z, x in zip(dataZ1[:-1], dataZ2, xvals[:-1]):
    axs[1].plot([x, x], [d, z], ':', color=(.7, .7, .7), zorder=-10)

plt.tight_layout()
plt.savefig('dataQC_recalculatingZ.png')
