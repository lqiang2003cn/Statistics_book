# define global figure properties used for publication

import matplotlib.pyplot as plt
# define global figure properties used for publication
import matplotlib_inline.backend_inline
from scipy import stats

matplotlib_inline.backend_inline.set_matplotlib_formats('svg')  # display figures in vector format
plt.rcParams.update({'font.size': 14,  # font size
                     'savefig.dpi': 300,  # output resolution
                     'axes.titlelocation': 'left',  # title location
                     'axes.spines.right': False,  # remove axis bounding box
                     'axes.spines.top': False,  # remove axis bounding box
                     })

x = [4, 1, 2, 3, 3]

print(stats.rankdata(x))
