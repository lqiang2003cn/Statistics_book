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

z = np.random.randint(-5, 6, size=10000)

plt.hist(z, bins=len(set(z)))
plt.tight_layout()
plt.savefig('simdat_random_int_hist.png')

z = np.round(np.random.randn(10000) * 10)
print(np.unique(z))
plt.hist(z)
plt.savefig('simdat_random_int_hist_z.png')
