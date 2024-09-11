import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

# the data
x1 = np.random.randn(100) - 0.5
x2 = np.random.randn(100) + 0.5
X = np.concatenate((x1, x2))

_, axs = plt.subplots(1, 4, figsize=(14, 4))

# regular histogram
axs[0].hist(X, bins='fd', color='gray', edgecolor='k')
axs[0].set_title(r'$\bf{A}$)  Step 1: histogram')
axs[0].set_ylim([0, 40])
axs[0].set_xlabel('Data value')
axs[0].set_ylabel('Count')

# smooth interpolation of histogram
y, x = np.histogram(X, bins='fd')
x = (x[:-1] + x[1:]) / 2

from scipy import interpolate

interpF = interpolate.interp1d(x, y, kind='cubic')
xx = np.linspace(x[0], x[-1], 100)
yy = interpF(xx)

axs[1].plot(xx, yy, 'k')
axs[1].set_xlabel('Data value')
axs[1].set_ylabel('Count')
axs[1].set_ylim([0, 40])
axs[1].set_title(r'$\bf{B}$)  Step 2: interpolate')

# now for the violin plot (as a dataframe to use seaborn)
df = pd.DataFrame(X)
sns.violinplot(data=df, palette='gray', ax=axs[2])
sns.stripplot(data=df, ax=axs[2], palette='dark:#b2b2b2')
axs[2].set_xlabel('Count (norm.)')
axs[2].set_ylabel('Data value')
axs[2].set_title(r'$\bf{C}$)  Step 3: rotate/mirror')

# NOTE: The code below is actually a solution to Exercise 7, so don't inspect this code
#       too carefully if you want the challenge of solving it yourself :)
df = pd.DataFrame(np.vstack((x1, x2)).T, columns=['x1', 'x2'])
df_all = pd.DataFrame(pd.concat((df['x1'], df['x2']), axis=0), columns=['y'])
df_all['distr'] = 'x2'
df_all['distr'][:len(df)] = 'x1'  # note: you can safely ignore the warning that this line produces
df_all[''] = ' '
sns.violinplot(data=df_all, x='', y='y', palette='gray', ax=axs[3], split=True, hue='distr')
axs[3].legend_.remove()
axs[3].set(xlim=[-.75, .75], ylabel='Data value')
axs[3].set_title(r'$\bf{D}$)  Asymmetric violin')

plt.tight_layout()
plt.savefig('vis_makeAviolin.png')
