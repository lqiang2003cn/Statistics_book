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

# the key factor to manipulate
stds = np.linspace(0.01,10,40)

# parameters to hold constant
samplesize = 100
mean = 0


# initialize results matrix
results = np.zeros(len(stds))


# start the experiment
for stdi in range(len(stds)):

  # data parameters for this experiment run
  thisStd = stds[stdi]

  # generate data
  data = np.random.normal(mean,thisStd,samplesize)

  # collect results
  results[stdi] = np.mean(data)


# plot the results
plt.figure(figsize=(8,4))
plt.plot(stds,results,'ks',markersize=10,markerfacecolor=(.9,.9,.9))

# add to the plot
plt.axhline(mean,linestyle='--',color=(.3,.3,.3),zorder=-1)
plt.xlabel('Population standard deviation')
plt.ylabel('Empirical mean')

plt.tight_layout()
plt.savefig('simdat_experiment1.png')
