import numpy as np
from matplotlib import pyplot as plt

mongooses_africa = np.arctanh(np.random.uniform(size=100) * 1.5 - .75) * 12 + 37
mongooses_asia = np.arctanh(np.random.uniform(size=500) * 1.5 - .75) * 15 + 42

# create common bin boundaries across both datasets
alldata = np.concatenate((mongooses_africa, mongooses_asia))
binbounds = np.linspace(np.min(alldata), np.max(alldata), 30)

_, axs = plt.subplots(2, 2, figsize=(8, 6))

# top two panels show raw histograms
axs[0, 0].hist(mongooses_africa, bins=binbounds, color='gray', edgecolor='k')
axs[0, 0].set_xlim([binbounds[0] - 1, binbounds[-1] + 1])
axs[0, 0].set_ylim([0, 30])  # ylim hard-coded based on N and bins
axs[0, 0].set_title(r'$\bf{A}$)  Counts: African mons')

axs[0, 1].hist(mongooses_asia, bins=binbounds, color='gray', edgecolor='k')
axs[0, 1].set_xlim([binbounds[0] - 1, binbounds[-1] + 1])
axs[0, 1].set_ylim([0, 30])
axs[0, 1].set_title(r'$\bf{B}$)  Counts: Asian mons')

# bottom row for proportion: density = True means calculating proportion
axs[1, 0].hist(mongooses_africa, bins=binbounds, density=True, color='gray', edgecolor='k')
axs[1, 0].set_xlim([binbounds[0] - 1, binbounds[-1] + 1])
axs[1, 0].set_ylim([0, .1])
axs[1, 0].set_title(r'$\bf{C}$)  Proportion: African mons')

axs[1, 1].hist(mongooses_asia, bins=binbounds, density=True, color='gray', edgecolor='k')
axs[1, 1].set_xlim([binbounds[0] - 1, binbounds[-1] + 1])
axs[1, 1].set_ylim([0, .1])
axs[1, 1].set_title(r'$\bf{D}$)  Proportion: Asian mons')

plt.tight_layout()
plt.savefig('vis_mongeese_rawProp.png')
