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

# generate "population"
population = [1, 2, 3, 4]
for i in range(20):
    population = np.hstack((population, population))

nPop = len(population)
expval = np.mean(population)
print(f'Expected value (population mean): {expval}')
print(f'Population size: {nPop}')

## experiment: draw larger and larger samples

k = 1500  # maximum number of samples
sampleAves = np.zeros(k)

for i in range(k):
    # get a sample
    sample = np.random.choice(population, size=i + 1)

    # compute and store its mean
    sampleAves[i] = np.mean(sample)

# visualize!
plt.figure(figsize=(8, 4))
plt.plot(sampleAves, 's', markerfacecolor=(.9, .9, .9), color=(.6, .6, .6))
plt.plot([1, k], [expval, expval], 'k', linewidth=4)
plt.xlabel('Sample size')
plt.ylabel('Value')
plt.xlim([-20, k + 20])
plt.ylim([np.min(sampleAves) * .85, 1.05 * np.max(sampleAves)])
plt.legend(('Sample average', 'Population average'))

plt.tight_layout()
plt.savefig('sample_LLNdemo1.png')
