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

# outlier threshold
zThreshold = 3.29

# create some raw data
N = 135
data = np.exp(np.random.randn(N) / 2) + 5

# zscore the data
dataZ = (data - np.mean(data)) / np.std(data, ddof=1)

# identify data indices containing outliers
outliers = np.where(np.abs(dataZ) > zThreshold)[0]

# and plot
_, axs = plt.subplots(1, 2, figsize=(10, 4))
axs[0].plot(data, 'ks', markersize=10, markerfacecolor=(.7, .7, .7))
axs[0].set(xlim=[-2, N + 1], xlabel='Data index', ylabel='Data value')
axs[0].set_title(r'$\bf{A}$)  Original data')

axs[1].plot(dataZ, 'ks', markersize=10, markerfacecolor=(.9, .9, .9))
axs[1].axhline(zThreshold, linestyle='--', color=(.9, .9, .9))
axs[1].plot(outliers, dataZ[outliers], 'kx', markersize=10, markeredgewidth=2)
axs[1].set(xlim=[-3, N + 2], xlabel='Data index', ylabel='Transformed data value')
axs[1].set_title(r'$\bf{B}$)  Z-transformed data')

plt.tight_layout()
plt.savefig('dataQC_zMethodOutliers.png')
