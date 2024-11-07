# import libraries and define global settings
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

# create two data variables
x = np.linspace(0,6*np.pi,10000)
s = 10*np.sin(x)
u = 2*np.random.rand(len(x))-1


# only difference from the previous figure is the amplitude-scaling!


# combine them into a list for convenience
datasets = [ s,u,s+u ]
axislets = iter('ABCDEF') # axis labels


# plot!
_,axs = plt.subplots(3,2,figsize=(7,6))

for i in range(3):

  # axis variable label
  dlab = str(i+1) if i<2 else '1+2'

  # plot the data
  axs[i,0].plot(x,datasets[i],'k.',markersize=1)
  axs[i,0].set_title(r'$\bf{%s}$)  Data %s' %(next(axislets),dlab))

  # plot the histogram
  axs[i,1].hist(datasets[i],bins=200,color='k',edgecolor=None)
  axs[i,1].set_title(r'$\bf{%s}$)  Histogram %s' %(next(axislets),dlab))


# adjust the axis properties
for a in axs.flatten():
  a.xaxis.set_visible(False)
  a.spines['bottom'].set_visible(False)

plt.tight_layout()
plt.savefig('sample_CLTdemo3b.png')
plt.show()