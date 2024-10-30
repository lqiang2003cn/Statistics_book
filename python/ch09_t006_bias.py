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

N = 512
X = np.random.rand(N,2)

# nonrandom sorting
X = X[np.argsort(np.sum(X**2,axis=1)),:]


# plot all data points
plt.figure(figsize=(8,6))
plt.plot(X[:,0],X[:,1],'s',color=(.7,.7,.7),markerfacecolor='w',markersize=10)


# nonrandom sampling to simulate a bias
sampmeans = np.zeros((6,2)) # hard-coded to 6 samples...
sampbias = np.linspace(20,N-40,6,dtype=int)
shapes = 'o^d*XP'
colors = 'brmkgc'
for si in range(6):

  # biased sample and its mean
  sample = X[sampbias[si]:sampbias[si]+40,:]
  sampmeans[si,:] = np.mean(sample,axis=0)

  # plot samples
  plt.plot(sample[:,0],sample[:,1],shapes[si],color=colors[si],
           markerfacecolor=colors[si],label=f'Sample {si+1}')

  # plot sample mean
  plt.plot(sampmeans[si,0],sampmeans[si,1],shapes[si],color='k',
           markerfacecolor=colors[si],markersize=15)



# plot the average of sample means
plt.plot(np.mean(sampmeans[:,0]),np.mean(sampmeans[:,1]),'ko',
         markerfacecolor='k',markersize=20,label='Average of means')

plt.xticks([])
plt.yticks([])
plt.xlabel('Variable 1')
plt.ylabel('Variable 2')
plt.legend(bbox_to_anchor=[1,1.02])

plt.tight_layout()
plt.savefig('sample_meanOfSamplesGeom_biased.png')
