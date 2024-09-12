# generate some data
import numpy as np
from matplotlib import pyplot as plt

timesWatched = np.round( np.abs(np.random.randn(500)*20) )/2

# force an outliner
timesWatched[300] = 35

_,axs = plt.subplots(1,2,figsize=(10,4))

axs[0].plot(timesWatched,'ks')
axs[0].set_xlabel('Respondent index')
axs[0].set_ylabel('Times watched')
axs[0].set_title(r'$\bf{A}$)  Visualized by respondent ID#')

axs[1].hist(timesWatched,bins='fd',color='gray',edgecolor='k')
axs[1].set_xlabel('Times watched')
axs[1].set_ylabel('Count')
axs[1].set_title(r'$\bf{B}$)  Visualized as histogram')

plt.tight_layout()
plt.savefig('desc_YT_visualize.png')