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

# Create normally distributed data
N = 100
data = np.random.randn(N)

# and add two random outliers in random positions
data[np.random.choice(np.arange(N), 2)] = np.random.uniform(2, 3, 2) ** 2

# and plot
plt.figure(figsize=(8, 4))
plt.plot(data, 'ks', markersize=10, markerfacecolor=(.7, .7, .7))
plt.xlim([-2, N + 1])
plt.xlabel('Data index')
plt.ylabel('Data value')

plt.tight_layout()
plt.savefig('dataQC_example2outliers.png')
