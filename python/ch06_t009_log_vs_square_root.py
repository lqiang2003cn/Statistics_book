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

# some right-tailed non-normally distributed data
X = np.random.randn(10000) ** 2

y_r, x_r = np.histogram(X, bins=100)  # r = raw
y_l, x_l = np.histogram(np.log(X), bins=100)  # l = log
y_s, x_s = np.histogram(np.sqrt(X), bins=100)  # s = sqrt

_, axs = plt.subplots(1, 3, figsize=(10, 4))

# theory
q = np.linspace(.1, 10, 100)
axs[0].plot(q, np.log(q), 'k', linewidth=3, label='ln(x)')
axs[0].plot(q, np.sqrt(q), '--', color='gray', linewidth=3, label='sqrt(x)')
axs[0].set(xlim=[0, 10], xlabel='Raw data value', ylabel='Transformed data value')
axs[0].set_title(r'$\bf{A}$)  Transformation')
axs[0].legend()

# untransformed data
axs[1].plot((x_r[1:] + x_r[:-1]) / 2, y_r, 'k', linewidth=2)
axs[1].set(xlabel='Raw data value', ylabel='Count')
axs[1].set_title(r'$\bf{B}$)  Data histogram')

axs[2].plot((x_l[1:] + x_l[:-1]) / 2, y_l, 'k', linewidth=2, label='ln(x)')
axs[2].plot((x_s[1:] + x_s[:-1]) / 2, y_s, '--', color='gray', linewidth=2, label='sqrt(x)')
axs[2].set(xlabel='Transformed data value', ylabel='Count')
axs[2].set_title(r'$\bf{C}$)  Trans data hist.')
axs[2].legend()

plt.tight_layout()
plt.savefig('trans_logsqrt.png')
