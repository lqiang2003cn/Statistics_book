import numpy as np
import matplotlib.pyplot as plt

# define global figure properties used for publication
import matplotlib_inline.backend_inline

matplotlib_inline.backend_inline.set_matplotlib_formats('svg')  # display figures in vector format
plt.rcParams.update({'font.size': 14,  # font size
                     'savefig.dpi': 300,  # output resolution
                     'axes.titlelocation': 'left',  # title location
                     'axes.spines.right': False,  # remove axis bounding box
                     'axes.spines.top': False,  # remove axis bounding box
                     })

# some data
X = np.random.weibull(2,5000)

# create a histogram
plt.figure(figsize=(8,4))
plt.hist(X,'fd',color=(.8,.8,.8),edgecolor='k')
plt.xlabel('Data values')
plt.ylabel('Counts')
plt.title('Example Weibull distribution',loc='center')

plt.tight_layout()
plt.savefig('simdat_weibull.png')
