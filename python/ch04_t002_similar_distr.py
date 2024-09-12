# generate some data
import numpy as np
from matplotlib import pyplot as plt

sampleA = np.random.randn(1500) * 2 + np.pi ** np.pi
sampleB = np.random.randn(1500) * 2 + np.pi ** np.pi

_, axs = plt.subplots(1, 2, figsize=(10, 4))

axs[0].hist(sampleA, bins='fd', color='k', edgecolor='w')
axs[0].set(xlabel='Data value', ylabel='Count', xlim=[30, 45])
axs[0].set_title(r'$\bf{A}$)  Sample "A"')

axs[1].hist(sampleB, bins='fd', color='k', edgecolor='w')
axs[1].set(xlabel='Data value', ylabel='Count', xlim=[30, 45])
axs[1].set_title(r'$\bf{B}$)  Sample "B"')

plt.tight_layout()
plt.savefig('desc_rand_diffHists.png')
