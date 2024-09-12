# generate some data
import numpy as np
from matplotlib import pyplot as plt

# bimodal
_, axs = plt.subplots(2, 2, figsize=(10, 7))

# normal distribution with kurtosis
X = np.arctanh(np.random.rand(10000) * 1.8 - .9) + 1.5
axs[0, 0].hist(X, bins='fd', color=(.4, .4, .4), edgecolor='k')
axs[0, 0].set_xlabel('Data value')
axs[0, 0].set_ylabel('Bin count')
axs[0, 0].set_title(r'$\bf{A}$)')

# uniform distribution
X = np.random.rand(1000)
axs[0, 1].hist(X, bins='fd', color=(.4, .4, .4), edgecolor='k')
axs[0, 1].set_xlabel('Data value')
axs[0, 1].set_ylabel('Bin count')
axs[0, 1].set_title(r'$\bf{B}$)')

# power distribution
f = np.linspace(1, 10, 5001)
X = 1 / f + np.random.randn(len(f)) / 200
X[X > .9] = .9  # some clipping
axs[1, 0].hist(X, bins='fd', color=(.4, .4, .4), edgecolor='k')
axs[1, 0].set_xlabel('Data value')
axs[1, 0].set_ylabel('Bin count')
axs[1, 0].set_title(r'$\bf{C}$)')

# bimodal distribution
x1 = np.random.randn(500) - 2
x2 = np.random.randn(2500) + 2
X = np.concatenate((x1, x2))
axs[1, 1].hist(X, bins='fd', color=(.4, .4, .4), edgecolor='k')
axs[1, 1].set_xlabel('Data value')
axs[1, 1].set_ylabel('Bin count')
axs[1, 1].set_title(r'$\bf{D}$)')

plt.tight_layout()
plt.savefig('desc_exampleEmpHists.png')
