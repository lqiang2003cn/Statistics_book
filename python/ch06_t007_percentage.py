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

# Note: This code does not correspond to any figure in the book;
#  I include it here to illustrate the code.
#  Notice in the graph how the 'ref' data value turns into 0.

# a range of values for "new"
new = np.linspace(3, 210, 31)

# reference value
ref = 135

# compute percent change
pctchg = 100 * (new - ref) / ref

# visualize the transformed data
plt.figure(figsize=(6, 6))
plt.plot(new, pctchg, 'ks-', markerfacecolor='m', zorder=30)
plt.axhline(0, color='k', linestyle='--')
plt.axvline(ref, color='k', linestyle='--')
plt.xlabel('Original data values')
plt.ylabel('Transformed data values')
plt.title('Percent change', loc='center')
plt.grid()
plt.savefig('trans_percentage')