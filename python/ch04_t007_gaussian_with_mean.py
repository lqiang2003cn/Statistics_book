# generate some data
import numpy as np
from matplotlib import pyplot as plt

# generate a Laplace distribution
x1 = np.exp(-np.abs(3 * np.random.randn(4000)))
x2 = np.exp(-np.abs(3 * np.random.randn(4000)))
x = x1 - x2 + 1

# and compute its mean
xBar = np.mean(x)

# histogram
plt.figure(figsize=(6, 6))
plt.hist(x, bins='fd', color=(.7, .7, .7), edgecolor='k')

# vertical line for mean
plt.plot([xBar, xBar], plt.gca().get_ylim(), '--', color='k', linewidth=4)

plt.legend(['Mean', 'Histogram'])
plt.xlabel('Value')
plt.ylabel('Count')

plt.tight_layout()
plt.savefig('desc_distrWithMean.png')
