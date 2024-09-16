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

#%%
s = [1,2,np.pi,10]
print(np.random.choice(s,1))
#%%
# not limited to numbers
t = ['a','b','hello']
print(np.random.choice(t,1))
#%% select 4 elements randomly from s: an element can be selected multiple times: replace the selected one back to the set
print(np.random.choice(s,4))
#%% an element cannot be selected multiple times
print(np.random.choice(s,4,replace=False))
#%%

