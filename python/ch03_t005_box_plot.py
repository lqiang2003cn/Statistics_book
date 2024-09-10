import numpy as np
from matplotlib import pyplot as plt

data = np.random.randn(100)
data[data>2] = 1
data[data<-2] = -1
data[-1] = 3 # force one outlier



plt.figure(figsize=(2,4))

# draw the boxplot and make some color adjustments
h = plt.boxplot(data,patch_artist=True)
h['boxes'][0].set(color='k')
h['medians'][0].set(color='r')

plt.xlim([.8,1.5])
plt.xticks([])
plt.ylabel('Data values')

plt.tight_layout()
plt.savefig('vis_boxplotBasic.png')