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

a, b = np.sort(np.random.randint(-3, 11, 2))
N = 1001

Y = np.random.uniform(a, b, size=N)

print(a, b, np.min(a), np.max(b))
print('')
print(np.mean(Y), (a + b) / 2, np.median(Y))
print(np.var(Y, ddof=1), (b - a) ** 2 / 12)

# parameters for the distributions
aa = [-1, 0, 2, 1]
bb = [1, 0.1, 3, 1.6]
samplesize = 2500

_, axs = plt.subplots(2, 2, figsize=(10, 8))

for idx, axis in enumerate(axs.flatten()):
    # generate some data
    X = np.random.uniform(aa[idx], bb[idx], size=samplesize)

    # compute empirical boundaries
    bndL = np.min(X)
    bndU = np.max(X)

    # draw the histogram using the F-D rule for bin width
    axis.hist(X, bins='fd', color='gray', edgecolor='gray')
    axis.set(xlim=[-1.5, 3.5], ylabel='Count')
    axis.set_title(f'a={aa[idx]}, min(Y)={bndL:.3f}\n b={bb[idx]}, max(Y)={bndU:.3f}', loc='center')

plt.tight_layout()
plt.savefig('simdat_uniform4examples.png')
