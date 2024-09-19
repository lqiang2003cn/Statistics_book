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

N = 1000

# uniform data in range [-1,1]
Y = np.random.uniform(-1, 1, size=N)
# Note: Fisher-z is undefined for Y==|1|, but the probability of that happening in
#       random uniform data is so vanishingly small that coding an exception is unnecessary.

# transform
fY = np.arctanh(Y)

_, axs = plt.subplots(1, 3, figsize=(10, np.pi))

axs[0].hist(Y, 30, color=(.8, .8, .8), edgecolor='k')
axs[0].set(xlabel='Data values', ylabel='Count')
axs[0].set_title(r'$\bf{A}$)  Raw data hist.')

axs[1].hist(fY, 30, color=(.8, .8, .8), edgecolor='k')
axs[1].set(xlim=[-5, 5], xlabel='Data values', ylabel='Count')
axs[1].set_title(r'$\bf{B}$)  Fisher data hist.')

axs[2].plot(Y, fY, 'k.')
axs[2].set_title(r'$\bf{C}$)  Transformation')
axs[2].set(xlabel='Original data', ylabel='Transformed data')

plt.tight_layout()
plt.savefig('trans_fisherz.png')
