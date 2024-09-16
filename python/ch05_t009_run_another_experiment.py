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

## the next experiment with two factors to manipulate

# the key factors to manipulate
stds = np.linspace(0.01, 10, 40)
samplesizes = [100, 10000]

# parameters to hold constant
meanvalue = 0

# initialize results matrix
results = np.zeros((len(stds), len(samplesizes)))

# start the experiment
for stdi in range(len(stds)):

    for sampi in range(len(samplesizes)):
        # data parameters for this experiment run
        thisStd = stds[stdi]
        thisN = samplesizes[sampi]

        # generate data
        data = np.random.normal(meanvalue, thisStd, samplesizes[sampi])

        # collect results
        results[stdi, sampi] = np.mean(data)

# plot the results
plt.figure(figsize=(8, 4))
plt.plot(stds, results[:, 0], 'ks', markersize=10, markerfacecolor=(.9, .9, .9), label=f'N = {samplesizes[0]}')
plt.plot(stds, results[:, 1], 'ko', markersize=10, markerfacecolor=(.5, .5, .5), label=f'N = {samplesizes[1]}')

plt.axhline(meanvalue, linestyle='--', color=(.3, .3, .3), zorder=-1)

plt.xlabel('Population standard deviation')
plt.ylabel('Empirical mean')

plt.legend(loc='upper left')
plt.tight_layout()
plt.savefig('simdat_experiment2.png')
