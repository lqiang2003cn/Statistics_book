# define global figure properties used for publication

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

x = np.random.normal(250, 58, size=28)
zx = (x - np.mean(x)) / np.std(x, ddof=1)

plt.figure(figsize=(4, 4))
plt.plot(x, zx, 'ks', markersize=10, markerfacecolor=(.4, .4, .4), alpha=.6)
plt.xlabel('Original data')
plt.ylabel('Z-transformed data')

plt.tight_layout()
plt.savefig('trans_zRelativelyEqual.png')
