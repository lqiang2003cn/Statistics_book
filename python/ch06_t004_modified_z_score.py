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

# Some non-normal data
x1 = np.random.randn(500) + 2.5
x2 = np.random.randn(2500) - 2
y = np.concatenate((x1, x2))
y = y - np.min(y) + 3

# regular z-score
y_z = (y - np.mean(y)) / np.std(y, ddof=1)

# modified z
MAD = np.median(np.abs(y - np.median(y)))
y_zm = stats.norm.ppf(3 / 4) * (y - np.median(y)) / MAD

# their histograms
yy_z, xx_z = np.histogram(y_z, bins='fd')
yy_zm, xx_zm = np.histogram(y_zm, bins='fd')

_, axs = plt.subplots(1, 3, figsize=(10, 4))

axs[0].hist(y, bins='fd', color=(.9, .9, .9), edgecolor='k')
axs[0].set(xlabel='Data value', ylabel='Counts', title=r'$\bf{A}$)  Original data dist.')

axs[1].plot((xx_z[1:] + xx_z[:-1]) / 2, yy_z, linewidth=2, color='k', label='Regular')
axs[1].plot((xx_zm[1:] + xx_zm[:-1]) / 2, yy_zm, '--', linewidth=2, color=(.4, .4, .4), label='Modified')
axs[1].legend(loc='upper right', frameon=False, bbox_to_anchor=[1.08, 1.05])
axs[1].set(xlabel='Transformed value', ylabel='Counts', title=r'$\bf{B}$)  Z-score dists.')

axs[2].plot(y_z, y_zm, 'ko', markerfacecolor='w')
xval = np.min([np.min(y_z), np.min(y_zm)])
yval = np.max([np.max(y_z), np.max(y_zm)])
axs[2].plot([xval, yval], [xval, yval], '--', color=(.6, .6, .6), label='Unity')
axs[2].set(xlabel='"Regular" z', ylabel='Modified z', title=r'$\bf{C}$)  Comparison')
axs[2].legend()

plt.tight_layout()
plt.savefig('trans_modVreg_zscore.png')
