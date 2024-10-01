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

# with raw numerical data values
x = np.linspace(-6, 6, 81)
s = np.exp(x) / np.sum(np.exp(x))

_, axs = plt.subplots(1, 2, figsize=(10, 4))

for a in axs:
    a.plot(x, s, 'k-', linewidth=2)
    a.set(xlabel='Raw data values', ylabel='Softmaxified values', xlim=x[[0, -1]])

# scale y to log
axs[1].set_yscale('log')
axs[0].set_title(r'$\bf{A}$)  In linear space')
axs[1].set_title(r'$\bf{B}$)  In log space')

plt.tight_layout()
plt.savefig('prob_softmaxNumbers.png')
