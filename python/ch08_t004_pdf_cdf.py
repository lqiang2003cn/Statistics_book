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

# distribution
x = np.linspace(-5, 5, 501)
pdf = stats.norm.pdf(x)
cdf = stats.norm.cdf(x)

_, ax = plt.subplots(1, figsize=(7, 3))

# patch for the summed area
from matplotlib.patches import Polygon

bndi = np.argmin(np.abs(x - 1))
dots = np.zeros((bndi + 2, 2))
for i in range(bndi + 1):
    dots[i, :] = x[i], pdf[i]
dots[-1, :] = x[bndi], 0
ax.add_patch(Polygon(dots[:, [0, 1]], facecolor='k', alpha=.4))

# plot the functions
ax.plot(x, pdf, 'k--', linewidth=2, label='pdf')
ax.plot(x, cdf, 'k', linewidth=2, label='cdf')
ax.axvline(1, color='k', linestyle=':')

# make the plot a bit nicer
ax.set(xlim=x[[0, -1]], ylim=[0, 1.02], xlabel='Data value', ylabel='Probability')
plt.legend(loc='upper left')

plt.tight_layout()
plt.savefig('prob_pdf2cdf.png')
