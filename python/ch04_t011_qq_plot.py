# generate some data
import numpy as np
from matplotlib import pyplot as plt
from scipy import stats

N = 1000
d1 = np.random.randn(N)  # normal
d2 = np.exp(d1 * .8)  # non-normal

# data for histograms
y1, x1 = np.histogram(d1, bins=40)
y1 = y1 / np.max(y1)
x1 = (x1[:-1] + x1[1:]) / 2

y2, x2 = np.histogram(d2, bins=40)
y2 = y2 / np.max(y2)
x2 = (x2[:-1] + x2[1:]) / 2

# analytic normal distribution
x = np.linspace(-4, 4, 10001)
norm = stats.norm.pdf(x)
norm = norm / np.max(norm)

## now generate the plots
_, axs = plt.subplots(2, 2, figsize=(10, 7))
axs[0, 0].plot(x1, y1, 'k', linewidth=2, label='Empirical')
axs[0, 0].plot(x, norm, '--', color='gray', linewidth=2, label='Analytic')
axs[0, 0].legend()
axs[0, 0].set_xlabel('Data value')
axs[0, 0].set_ylabel('Probability (norm.)')
axs[0, 0].set_title(r'$\bf{A}$)  Distributions')

axs[0, 1].plot(x2, y2, 'k', linewidth=2, label='Empirical')
axs[0, 1].plot(x, norm, '--', color='gray', linewidth=2, label='Analytic')
axs[0, 1].legend()
axs[0, 1].set_xlabel('Data value')
axs[0, 1].set_ylabel('Probability (norm.)')
axs[0, 1].set_title(r'$\bf{B}$)  Distributions')

# QQ plots
stats.probplot(d1, plot=axs[1, 0], fit=True)
stats.probplot(d2, plot=axs[1, 1], fit=True)

for i in range(2):
    axs[1, i].get_lines()[0].set(markerfacecolor='r', markeredgecolor='b')
    axs[1, i].get_lines()[1].set(color='y', linewidth=3)
    axs[1, i].set_title(' ')
    axs[1, i].set_ylabel('Data values (sorted)')

axs[1, 0].set_title(r'$\bf{C}$)  QQ plot')
axs[1, 1].set_title(r'$\bf{D}$)  QQ plot')

plt.tight_layout()
plt.savefig('desc_qq.png')
