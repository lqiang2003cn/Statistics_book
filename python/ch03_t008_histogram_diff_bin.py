import numpy as np
from matplotlib import pyplot as plt

X = [1, 2, 2, 3, 3, 4, 5, 5, 5, 5, 6, 7, 7, 7, 8, 8, 9]

plt.figure(figsize=(8, 4))
plt.hist(X, bins=np.arange(0.5, 9.51, step=1), color='gray', edgecolor='k')
plt.xticks(np.arange(np.min(X), np.max(X) + 1))
plt.xlabel('Numerical value')
plt.ylabel('Count')

plt.tight_layout()
plt.savefig('vis_histOfInts2.png')

_, x1 = np.histogram(X, bins=len(set(X)))
_, x2 = np.histogram(X, np.arange(.5, 9.51, step=1))

for i in range(len(x1) - 1):
    print(f'Bin {i + 1}:  [{x1[i]:.1f} , {x1[i + 1]:.1f}]   [{x2[i]:.1f} , {x2[i + 1]:.1f}]')


