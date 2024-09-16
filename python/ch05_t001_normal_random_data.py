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

# parameters for the distributions
means = [-1, 0, 1, 3]
stds = [1, .1, 3, 1.6]
samplesize = 2500

_, axs = plt.subplots(2, 2, figsize=(10, 8))

for idx, axis in enumerate(axs.flatten()):
    # generate some data
    X = np.random.normal(loc=means[idx], scale=stds[idx], size=samplesize)

    # compute empirical mean and std
    empave = np.mean(X)
    empstd = np.std(X, ddof=1)

    # draw the histogram using the F-D rule for bin width
    axis.hist(X, bins='fd', color='gray', edgecolor='gray')
    axis.set(xlim=[-15, 15], ylabel='Count')
    axis.set_title(f'$\\mu$={means[idx]}, $\\overline{{X}}$={empave:.3f}\n$\\sigma$={stds[idx]}, std(X)={empstd:.3f}', loc='center')

plt.tight_layout()
plt.savefig('simdat_normal4examples.png')
