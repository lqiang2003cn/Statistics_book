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

# %%
# categorical probability data
categoryLabels = ['SUV', 'Convert.', 'Sports', 'Minivan', 'Coupe']
categoryData = np.random.randint(low=5, high=30, size=len(categoryLabels)).astype(np.float64)
categoryData /= np.sum(categoryData)

# discrete numerical probability data
empiricalIQ = np.random.normal(loc=100, scale=15, size=100)

# continuous (analytic) probability data
x = np.linspace(-4, 4, 101)
continuousData = stats.norm.pdf(x) * 15 + 100

### visualize!
_, axs = plt.subplots(1, 3, figsize=(10, 3))

# categorical data in bars
axs[0].bar(categoryLabels, categoryData, color=[.8, .8, .8], edgecolor='k')
axs[0].set_title(r'$\bf{A}$)  pmf of car types')
axs[0].set(ylabel='Probability', yticks=[])
axs[0].tick_params(axis='x', rotation=45)

# empirical probability data that estimate a density, still in bars
axs[1].hist(empiricalIQ, bins=15, color=[.8, .8, .8], edgecolor='k')
axs[1].set(xlabel='IQ', ylabel='Probability', yticks=[], xlim=[40, 160])
axs[1].set_title(r'$\bf{B}$)  pmf of IQ')

# analytical probability density as a line
axs[2].plot(x * 15 + 100, continuousData, 'k')
axs[2].set(xlabel='IQ', ylabel='Probability', yticks=[], xlim=[40, 160])
axs[2].set_title(r'$\bf{C}$)  pdf of IQ')

plt.tight_layout()
plt.savefig('prob_visualizeMassDensity.png')
