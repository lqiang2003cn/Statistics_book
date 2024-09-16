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

l = np.arange(5)
print(l)
print(np.random.permutation(l))
# %%
# to randomly re-sort a dataset

theData = np.arange(-3, 4) ** 3
# %%
newIdx = np.random.permutation(len(theData))
shufData = theData[newIdx]

print(theData)
print(newIdx)
print(shufData)
# %%
