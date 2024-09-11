import numpy as np
from matplotlib import pyplot as plt

tempC = [ 26,25,23,19,15,11,11,13,16,19,22,25 ]
months = [ 'Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec' ]

# angles for plotting
theta = np.linspace(0,2*np.pi,len(months)+1)

# repeat first data point so the line wraps around
tempC.append(tempC[0])


## draw the data:using polar
ax = plt.subplot(111,polar=True)
ax.plot(theta,tempC,'ko-')
ax.fill(theta,tempC,'k',alpha=.1)

# make the plot look nicer
# mark the angles of 12 points
ax.set_xticks(theta[:-1])
ax.set_xticklabels(months)
ax.set_yticks([10,20,30])
ax.set_ylim([0,30])
ax.set_title('High temps ($^{\circ}$C) near Patagonia',y=1.15,loc='center')


plt.tight_layout()
plt.savefig('vis_radialGood.png')