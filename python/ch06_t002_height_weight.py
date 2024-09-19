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

# fake heights and weights, in units of cm and kg
N = 3425
height = np.arctanh(np.random.uniform(-.9, .8, size=N)) * 20 + 160 + np.random.randn(N) * 3
weight = np.arctanh(np.random.uniform(-.3, .99, size=N)) * 10 + 70 + np.random.randn(N) * 3

# our imaginary individual
ind_height = 177
ind_weight = 70

# z-score the distributions
height_z = (height - np.mean(height)) / np.std(height, ddof=1)
weight_z = (weight - np.mean(weight)) / np.std(weight, ddof=1)

# z-score the individual
ind_height_z = (ind_height - np.mean(height)) / np.std(height, ddof=1)
ind_weight_z = (ind_weight - np.mean(weight)) / np.std(weight, ddof=1)

# figure layout
_, axs = plt.subplots(2, 3, figsize=(12, 6))

# plot the values
axs[0, 0].axvline(ind_height, color='k', linestyle='--', linewidth=2)
axs[0, 0].set(xlabel='Height (cm)', yticks=[], xlim=[ind_height - 50, ind_height + 50])
axs[0, 0].set_title(r'$\bf{A}_1$)  Raw height')

axs[1, 0].axvline(ind_weight, color='k', linestyle='--', linewidth=2)
axs[1, 0].set(xlabel='Weight (kg)', yticks=[], xlim=[ind_weight - 20, ind_weight + 20])
axs[1, 0].set_title(r'$\bf{A}_2$)  Raw weights')

# plot the raw distributions with the individual
axs[0, 1].hist(height, bins='fd', color=(.5, .5, .5), edgecolor=(.8, .8, .8))
axs[0, 1].axvline(ind_height, color='k', linestyle='--', linewidth=2)
axs[0, 1].set(xlabel='Height (cm)', ylabel='Count', xlim=[ind_height - 50, ind_height + 50])
axs[0, 1].set_title(r'$\bf{B}_1$)  Histogram of raw heights')

axs[1, 1].hist(weight, bins='fd', color=(.5, .5, .5), edgecolor=(.8, .8, .8))
axs[1, 1].axvline(ind_weight, color='k', linestyle='--', linewidth=2)
axs[1, 1].set(xlabel='Weight (kg)', ylabel='Count', xlim=[ind_weight - 20, ind_weight + 20])
axs[1, 1].set_title(r'$\bf{B}_2$)  Histogram of raw weights')

# plot the z-normalized distributions
axs[0, 2].hist(height_z, bins='fd', color=(.9, .9, .9), edgecolor='k')
axs[0, 2].axvline(ind_height_z, color='k', linestyle='--', linewidth=2)
axs[0, 2].set(xlabel='Normalized height (z)', ylabel='Count', xlim=[-3, 3])
axs[0, 2].set_title(r'$\bf{C}_1$)  Histogram of z-heights')

axs[1, 2].hist(weight_z, bins='fd', color=(.9, .9, .9), edgecolor='k')
axs[1, 2].axvline(ind_weight_z, color='k', linestyle='--', linewidth=2)
axs[1, 2].set(xlabel='Normalized weight (z)', ylabel='Count', xlim=[-3, 3])
axs[1, 2].set_title(r'$\bf{C}_2$)  Histogram of z-weights')

# export
plt.tight_layout()
plt.savefig('trans_zscore_example.png')
