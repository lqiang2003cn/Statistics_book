# generate some data
import numpy as np
from matplotlib import pyplot as plt
from scipy import stats

# create data using F distribution
x = np.linspace(0, 4, 10001)
y = stats.f.pdf(x, 10, 100)
y = y / np.max(y)
yBar = np.sum(y) * np.mean(np.diff(x))

# plot the distributions
_, axs = plt.subplots(2, 1, figsize=(4, 5))
axs[0].plot(-x, y, 'k', linewidth=3)
axs[0].plot([-yBar, -yBar], [0, 1], 'k--')
axs[0].set_title(r'$\bf{A}$)  Left (negative) skew')
axs[0].set(xlim=-x[[-1, 0]])
axs[0].set_ylabel('Proportion')
axs[0].set_xlabel('Data value')
axs[0].text(-3.5, .7, r'$\sum (x-\overline{x})^3 < 0$')

m1 = -yBar
xv1 = -x
sg1 = np.sum(np.power((xv1 - m1), 3))
print('sg1:', sg1)



axs[1].plot(x, y, 'k', linewidth=3)
axs[1].plot([yBar, yBar], [0, 1], 'k--')
axs[1].set_title(r'$\bf{B}$)  Right (positive) skew')
axs[1].set(xlim=x[[0, -1]])
axs[1].text(2, .7, r'$\sum (x-\overline{x})^3 > 0$')


m2 = yBar
xv2 = x
sg2 = np.sum(np.power((xv2 - m2), 3))
print('sg2:', sg2)

for a in axs: a.set(xticks=[], yticks=[])

plt.tight_layout()
plt.savefig('desc_skew.png')
