import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
# simple data... just a line!
y = np.linspace(1,10**4)

# create a figure
_,axs = plt.subplots(1,3,figsize=(12,3.5))

# visualization
for i in range(3):

  # plot the line (same data in all plots!)
  axs[i].plot(y,'k',linewidth=2)

  # adjust the axes for the log plots
  if i>0:
    axs[i].set_yscale('log')
    t = r'$\bf{' + ['B','C'][i-1] + '}$)  Log scaling'
    axs[i].set_title(t)
    axs[i].set_ylabel('Spacing by multiplication')



# log scaling is in scientific notation by default;
# here I change it to scalar format.
from matplotlib.ticker import ScalarFormatter
axs[1].yaxis.set_major_formatter(ScalarFormatter())

# labels
axs[0].set_title(r'$\bf{A}$)  Linear scaling')
axs[0].set_ylabel('Spacing by addition')


plt.tight_layout()
plt.savefig('vis_linVlog_line.png')
