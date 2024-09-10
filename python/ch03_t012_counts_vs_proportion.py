import numpy as np
from matplotlib import pyplot as plt

data = np.random.rand(200) ** 2

# extract histogram data
counts, x = np.histogram(data, bins='fd')
# t
binCents = (x[:-1] + x[1:]) / 2

# convert counts to proportion
proportion = counts / np.sum(counts)

_, axs = plt.subplots(1, 2, figsize=(8, 4))

axs[0].bar(binCents, counts, width=.12, color='gray', edgecolor='k')
axs[0].set_title(r'$\bf{A}$)  Raw counts')
axs[0].set_ylabel('Count')

axs[1].bar(binCents, proportion, width=.12, color='gray', edgecolor='k')
axs[1].set_title(r'$\bf{B}$)  Proportion')
axs[1].set_ylabel('Proportion')

plt.tight_layout()
plt.savefig('vis_histCountVsProp.png')
