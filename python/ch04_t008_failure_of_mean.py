# generate some data
import numpy as np
from matplotlib import pyplot as plt

_, axs = plt.subplots(1, 2, figsize=(10, 3))

## case 1: mean does not reflect the most common value
data = [0, 0]
data[0] = (np.random.randn(400) + 2.5) ** 3 - 50

## case 2: bimodal distribution
x1 = np.random.randn(500) - 3
x2 = np.random.randn(500) + 3
data[1] = np.concatenate((x1, x2))

# histograms and means
for i in range(2):
    # data average
    xBar = np.mean(data[i])

    # histogram with vertical line for mean
    axs[i].hist(data[i], bins='fd', color='gray', edgecolor='k')
    axs[i].plot([xBar, xBar], axs[i].get_ylim(), '--', color='k', linewidth=4)
    axs[i].set_xlabel('Value')
    axs[i].set_ylabel('Count')

axs[0].set_title(r'$\bf{A}$)  Non-symmetric distribution')
axs[1].set_title(r'$\bf{B}$)  Bimodal distribution')

plt.tight_layout()
plt.savefig('desc_meanFailures.png')
