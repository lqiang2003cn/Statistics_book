# generate some data
import numpy as np
from matplotlib import pyplot as plt

# sample size and x-axis grid
N = 2345
x = np.linspace(1, 10, N)

# generate some data
ho = np.random.randn(N)
he = np.random.randn(N) * x

## visualize
_, axs = plt.subplots(1, 2, figsize=(10, 4))

axs[0].plot(x, ho, 'ko', markersize=10, markerfacecolor=(.7, .7, .7), alpha=.3)
axs[0].set(xlabel='Data index', xticks=[], yticks=[], ylabel='Data value')
axs[0].set_title(r'$\bf{A}$) Homoscedasticity')

axs[1].plot(x, he, 'ks', markersize=10, markerfacecolor=(.7, .7, .7), alpha=.3)
axs[1].set(xlabel='Data index', xticks=[], yticks=[], ylabel='Data value')
axs[1].set_title(r'$\bf{B}$) Heteroscedasticity')

plt.tight_layout()
plt.savefig('desc_homohetero.png')
