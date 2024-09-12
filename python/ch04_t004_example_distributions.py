# generate some data
import numpy as np
from matplotlib import pyplot as plt
from scipy import stats

x = np.linspace(-5, 5, 10001)

_, axs = plt.subplots(2, 2, figsize=(10, 7))

# Gaussian
y = stats.norm.pdf(x)  # stats.norm.pdf(x*1.5-2.7) + stats.norm.pdf(x*1.5+2.7)
axs[0, 0].plot(x, y, 'k', linewidth=3)
axs[0, 0].set_title(r'$\bf{A}$)  Gaussian ("bell curve")')
axs[0, 0].set_xlim(x[[0, -1]])

# T
axs[0, 1].plot(x, stats.t.pdf(x, 20), 'k', linewidth=3)
axs[0, 1].set_title(r'$\bf{B}$)  t distribution (df=20)')
axs[0, 1].set_xlim(x[[0, -1]])

# F
x = np.linspace(0, 10, 10001)
axs[1, 0].plot(x, stats.f.pdf(x, 5, 100), 'k', linewidth=3)
axs[1, 0].set_title(r'$\bf{C}$)  F distribution (df=5,100)')
axs[1, 0].set_xlim(x[[0, -1]])

# Chi
axs[1, 1].plot(x, stats.chi2.pdf(x, 3), 'k', linewidth=3)
axs[1, 1].set_title(r'$\bf{D}$)  Chi-square distribution (df=3)')
axs[1, 1].set_xlim(x[[0, -1]])

plt.tight_layout()
plt.savefig('desc_exampleDistributions.png')
