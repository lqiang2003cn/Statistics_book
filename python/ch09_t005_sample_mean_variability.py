# import libraries and define global settings
import matplotlib.pyplot as plt
# define global figure properties used for publication
import matplotlib_inline.backend_inline
import numpy as np

matplotlib_inline.backend_inline.set_matplotlib_formats('svg')  # display figures in vector format
plt.rcParams.update({'font.size': 14,  # font size
                     'savefig.dpi': 300,  # output resolution
                     'axes.titlelocation': 'left',  # title location
                     'axes.spines.right': False,  # remove axis bounding box
                     'axes.spines.top': False,  # remove axis bounding box
                     })

N = 512
X = np.random.rand(N, 2)

sample1 = X[np.random.choice(N, size=40), :]
sample2 = X[np.random.choice(N, size=40), :]

plt.figure(figsize=(8, 6))

# plot all data points
plt.plot(X[:, 0], X[:, 1], 's', color=(.7, .7, .7), markerfacecolor='w', markersize=10)

# plot sample data
plt.plot(sample1[:, 0], sample1[:, 1], 'bo')
plt.plot(sample2[:, 0], sample2[:, 1], 'r^')

# plot sample means
plt.plot(np.mean(sample1[:, 0]), np.mean(sample1[:, 1]), 'bo', markersize=15)
plt.plot(np.mean(sample2[:, 0]), np.mean(sample2[:, 1]), 'r^', markersize=15)

plt.xticks([])
plt.yticks([])
plt.xlabel('Variable 1')
plt.ylabel('Variable 2')
plt.legend(['All data', 'Sample 1', 'Sample 2', 'Mean s1', 'Mean s2'], bbox_to_anchor=[1, 1.02])

plt.tight_layout()
plt.savefig('sample_meanOfSamplesGeom.png')
