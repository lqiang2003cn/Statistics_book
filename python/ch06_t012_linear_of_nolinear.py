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

# %%
# sample size
N = 200

# the data (note how the nonlinearity is implemented)
x = np.linspace(.01, 3, N)
y = np.exp(x) + np.random.randn(N) * np.linspace(.1, 1, N) * 3
y = np.abs(y)

_, axs = plt.subplots(1, 2, figsize=(10, 4))

axs[0].plot(x, y, 'ko', markerfacecolor='w')
axs[0].set(xlabel='x', ylabel='y')
axs[0].set_title(r'$\bf{A})$  Original data')

axs[1].plot(x, np.log(y), 'ko', markerfacecolor='w')
axs[1].set(xlabel='x', ylabel='ln(y)')
axs[1].set_title(r'$\bf{B})$  Transformed data')

a, b = np.polyfit(x, np.log(y), 1)
axs[1].plot(x, a * x + b, 'k', linewidth=3)

plt.tight_layout()
plt.savefig('trans_linearizedFit.png')

plt.savefig("trans_linearizedFit.png")
