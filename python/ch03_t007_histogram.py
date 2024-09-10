import numpy as np
from matplotlib import pyplot as plt

X = [1, 2, 2, 3, 3, 4, 5, 5, 5, 5, 6, 7, 7, 7, 8, 8, 9]

plt.figure(figsize=(8, 4))
plt.hist(X, bins=len(set(X)), color='gray', edgecolor='k')
plt.xticks(np.arange(np.min(X), np.max(X) + 1))
plt.xlabel('Numerical value')
plt.ylabel('Count')

plt.tight_layout()
plt.savefig('vis_histOfInts1.png')
