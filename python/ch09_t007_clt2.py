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

# new population!
Npop = 1000000
population = np.random.randn(Npop)**2


# parameters and initializations
samplesize   =  30
numberOfExps = 500
samplemeans  = np.zeros(numberOfExps)

# run the experiment!
for expi in range(numberOfExps):
  # compute and store its mean
  samplemeans[expi] = np.mean( np.random.choice(population,size=samplesize) )


# show the results
fig,axs = plt.subplots(1,2,figsize=(10,4))

# histogram of the data
axs[0].hist(population,bins=50,color=[.8,.8,.8],edgecolor='k')
axs[0].set(xlabel='Data value',ylabel='Count')
axs[0].set_title(r'$\bf{A}$)  Distribution of population data')
axs[0].ticklabel_format(style='plain')

# histogram of the sample means
axs[1].hist(samplemeans,bins='fd',color=[.8,.8,.8],edgecolor='k')
axs[1].set(xlabel='Sample mean',ylabel='Count',xlim=[0,4])
axs[1].axvline(np.mean(population),linewidth=3,color='k',linestyle='--')
axs[1].set_title(r'$\bf{B}$)  Distribution of sample means')

plt.tight_layout()
plt.savefig('sample_CLTdemo2.png')
plt.show()