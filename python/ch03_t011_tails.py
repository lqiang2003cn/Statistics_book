import numpy as np
import scipy.stats as stats
from matplotlib import pyplot as plt

# create a Gaussian probability curve
x = np.linspace(-4, 4, 401)
gpdf = stats.norm.pdf(x)

# the find the indices of the 2.5% and 97.5%
lbndi = np.argmin(np.abs(x - stats.norm.ppf(.05)))
ubndi = np.argmin(np.abs(x - stats.norm.ppf(1 - .05)))

# plot the probability function and the vertical lines
_, ax = plt.subplots(1, figsize=(5, 4))
ax.plot(x, gpdf, 'k', linewidth=2)
ax.set(xlim=x[[0, -1]], ylim=[0, .42], xticks=[], yticks=[],
       xlabel='Data value', ylabel='Proportion')

# now create patches for the rejected area
# Note: fill_between() is usually more convenient (and I use it later); here I show how to add a polygon patch FYI.
from matplotlib.patches import Polygon

dots = np.zeros((lbndi+2,2))
for i in range(lbndi+1):
  dots[i,:] = x[i],gpdf[i]
dots[-1,:] = x[lbndi],0
ax.add_patch(Polygon(dots,facecolor='k',alpha=.4))

# repeat for the right lobe
dots = np.zeros((len(x)-ubndi+1,2))
for i in range(ubndi,len(x)):
  dots[i-ubndi,:] = x[i],gpdf[i]
dots[-1,:] = x[ubndi],0
ax.add_patch(Polygon(dots,facecolor='k',alpha=.4))

# annotations
tailx = np.argmin(np.abs(x--2.2))
ax.annotate('Left tail',xy=(x[tailx],gpdf[tailx]+.01),
            xytext=(x[tailx]-1.1,gpdf[tailx]+.08),ha='center',
            arrowprops={'color':'k'},weight='bold',size=16)
tailx = np.argmin(np.abs(x-2.2))
ax.annotate('Right tail',xy=(x[tailx],gpdf[tailx]+.01),
            xytext=(x[tailx]+1.1,gpdf[tailx]+.08),ha='center',
            arrowprops={'color':'k'},weight='bold',size=16)

# ax.axis('off')
plt.tight_layout()
plt.savefig('vis_distribution_tails.png')