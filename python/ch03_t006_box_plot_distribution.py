import numpy as np
from matplotlib import pyplot as plt

data = np.hstack((np.random.normal(loc=100, size=(200, 1), scale=10),
                  np.random.normal(loc=100, size=(200, 1), scale=2)))

# draw the boxplot and make some color adjustments
plt.figure(figsize=(3, 3))
h = plt.boxplot(data, patch_artist=True, widths=.7)
for (b, m) in zip(h['boxes'], h['medians']):
    b.set(color='k')
    m.set(color='w')

plt.xlim([.5, 2.5])
plt.xticks(range(1, 3), ['A', 'B'])
plt.tight_layout()
plt.savefig('vis_boxplotComp.png')
