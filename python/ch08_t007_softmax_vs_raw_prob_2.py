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

# %%
# with raw counts
x = np.linspace(0, 25, 21)
s = np.exp(x) / np.sum(np.exp(x))
p = x / np.sum(x)

plt.plot(x, s, 'k^-', markerfacecolor='w', markersize=8, label=f'Softmax (sum={np.sum(s)})')
plt.plot(x, p, 'ko-', markerfacecolor='w', markersize=8, label=f'Probability (sum={np.sum(p)})')
plt.legend()

plt.savefig('prob_table_softmax_2.png', bbox_inches='tight')
