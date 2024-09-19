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

X = [1, 4, -5, 2, 1]

mu = np.mean(X)
sigma = np.std(X, ddof=1)

X_z = (X - mu) / sigma
print(X_z)
# %%
print(f'       Original | z-transformed')
print(f'Mean:      {np.mean(X):.2f} | {np.mean(X_z):.2f}')
print(f'stdev:     {np.std(X, ddof=1):.2f} | {np.std(X_z, ddof=1):.2f}')
