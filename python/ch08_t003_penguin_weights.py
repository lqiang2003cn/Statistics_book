# import libraries and define global settings
import matplotlib.pyplot as plt
# define global figure properties used for publication
import matplotlib_inline.backend_inline
import numpy as np
from scipy import stats

matplotlib_inline.backend_inline.set_matplotlib_formats('svg')  # display figures in vector format
plt.rcParams.update({'font.size': 14,  # font size
                     'savefig.dpi': 300,  # output resolution
                     'axes.titlelocation': 'left',  # title location
                     'axes.spines.right': False,  # remove axis bounding box
                     'axes.spines.top': False,  # remove axis bounding box
                     })

penguins = np.arctanh(np.random.uniform(size=473) * 1.8 - .9) * 2 + 4.5

bin_edges = np.arange(np.min(penguins), np.max(penguins), step=.25)

plt.figure(figsize=(6, 4))
plt.hist(penguins, bins=bin_edges, density=True, color=[.8, .8, .8], edgecolor='k')
plt.xlabel('Penguin weight (kg)')
plt.ylabel('Probability')

plt.tight_layout()
plt.savefig('prob_penguinWeightProb.png')
