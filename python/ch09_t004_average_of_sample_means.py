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

population = [1, 2, 3, 4]
for i in range(20):
    population = np.hstack((population, population))

# parameters and initializations
samplesize = 30
numberOfExps = 50
samplemeans = np.zeros(numberOfExps)

# run the experiment!
for expi in range(numberOfExps):
    # compute and store its mean
    samplemeans[expi] = np.mean(np.random.choice(population, size=samplesize))

# show the results
fig, ax = plt.subplots(2, 1, figsize=(7, 5))

# each individual sample mean
ax[0].plot(samplemeans, 's', markerfacecolor=(.9, .9, .9), color=(.6, .6, .6))
ax[0].set_title(r'$\bf{A}$)  Each sample mean')
ax[0].set_xlabel('Sample number (s)')

# cumulative average over the samples
ax[1].plot(np.cumsum(samplemeans) / np.arange(1, numberOfExps + 1),
           's', markerfacecolor=(.9, .9, .9), color=(.6, .6, .6))
ax[1].set_title(r'$\bf{B}$)  Cumulative sample means')

# multiline xtick labels
xticks = np.arange(0, 51, 10)
ax[1].set_xticks(xticks, labels=[f's={i}\nN={i * samplesize}' for i in xticks])

# common axis modifications
for a in ax:
    a.plot([0, numberOfExps], [np.mean(population), np.mean(population)], 'k')
    a.set(ylabel='Mean value', xlim=[-.5, numberOfExps + .5],
          ylim=[np.min(samplemeans) * .85, 1.1 * np.max(samplemeans)])

totSS = np.arange(1, numberOfExps + 1) * samplesize

plt.tight_layout()
plt.savefig('sample_LLNdemo2.png')
