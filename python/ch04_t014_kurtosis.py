# generate some data
import numpy as np
from matplotlib import pyplot as plt

# generate the distributions
x = np.linspace(-3, 3, 10001)
g = [None] * 3
g[0] = np.exp(-0.5 * x ** 2)
g[1] = np.exp(-x ** 2)
g[2] = np.exp(-10 * x ** 4)

# generate the plot
s = ['--', '-', ':']
n = ['-ve kurtosis', 'No excess', '+ve kurtosis']
for i in range(3):
    plt.plot(x, g[i], color=(i / 3, i / 3, i / 3), linewidth=3, linestyle=s[i], label=n[i])

plt.legend(loc='upper right', bbox_to_anchor=[1.02, 1.02])
plt.xlim(x[[0, -1]])

plt.tight_layout()
plt.savefig('desc_kurtosis.png')
