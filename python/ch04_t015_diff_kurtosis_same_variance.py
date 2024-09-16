# generate some data
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy import stats

# use the following 5 lines to manipulate kurtosis
x1 = np.exp(-np.abs(3 * np.random.randn(4000)))
x2 = np.exp(-np.abs(3 * np.random.randn(4000)))
d1 = x1 - x2 + 1
d2 = np.random.rand(4000)
d3 = np.random.randn(4000)

# uncomment the following 3 lines to manipulate skew
# d1 = np.random.randn(4000)
# d2 = np.exp(np.random.randn(4000)/2)
# d3 = -np.exp(np.random.randn(4000)/2)

# gather into a list
data = [d1, d2, d3]

S = np.zeros((len(data), 4))
i = 0
datalabel = []

plt.figure(figsize=(4, 4))

for X in data:
    # optional normalization
    X = (X - np.mean(X)) / np.std(X)

    # histogram and plot
    y1, x1 = np.histogram(X, bins='fd')
    x1 = (x1[1:] + x1[:-1]) / 2
    y1 = 100 * y1 / np.sum(y1)
    plt.plot(x1, y1, linewidth=3, color=(i / 3, i / 3, i / 3))
    datalabel.append('d' + str(i + 1))

    # gather stats
    S[i, :] = np.mean(X), np.var(X, ddof=1), stats.skew(X), stats.kurtosis(X)
    i += 1

plt.legend(datalabel)
plt.xlim([np.min(x1), np.max(x1)])
plt.xlabel('Data value')
plt.ylabel('Percentage')

plt.tight_layout()

plt.savefig('desc_diff_kurtosis_same_variance.png')
df = pd.DataFrame(S.T,columns=datalabel,index=['Mean','Variance','Skew','Kurtosis'])
from IPython.display import display
with pd.option_context('display.float_format','{:5.3f}'.format):
  display(df)