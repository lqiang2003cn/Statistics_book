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

_, axs = plt.subplots(1, 3, figsize=(10, 3))

# Gaussian
x = np.linspace(-5, 5, 101)
axs[0].plot(x, stats.norm.pdf(x), 'k--', linewidth=2)
axs[0].plot(x, stats.norm.cdf(x), 'k', linewidth=2)
axs[0].set_title(r'$\bf{A}$)  Normal')
axs[0].set_xlim(x[[0, -1]])

# F
x = np.linspace(0, 6, 101)
axs[1].plot(x, stats.f.pdf(x, 5, 100), 'k--', linewidth=2)
axs[1].plot(x, stats.f.cdf(x, 5, 100), 'k', linewidth=2)
axs[1].set_title(r'$\bf{B}$)  F')
axs[1].set_xlim(x[[0, -1]])

# semicircular
x = np.linspace(-1.5, 1.5, 101)
axs[2].plot(x, stats.semicircular.pdf(x), 'k--', linewidth=2)
axs[2].plot(x, stats.semicircular.cdf(x), 'k', linewidth=2)
axs[2].set_title(r'$\bf{C}$)  Semicircular')
axs[2].set_xlim(x[[0, -1]])

# legends
for a in axs: a.legend(['pdf', 'cdf'], frameon=False)

plt.tight_layout()
plt.savefig('prob_examplePdfCdf.png')
