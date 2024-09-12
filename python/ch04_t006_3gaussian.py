# generate some data
import numpy as np
from matplotlib import pyplot as plt

# function variable
x = np.linspace(-4, 4, 101)

# sigma
ss = [1, .3, 1]
# mu
cs = [0, 0, -1]

colors = ['k', (.7, .7, .7), (.4, .4, .4)]
styles = ['-', '--', ':']

plt.figure(figsize=(8, 4))

for s, c, col, sty in zip(ss, cs, colors, styles):
    # create gaussian
    gaus = np.exp(-(x - c) ** 2 / (2 * s ** 2))
    plt.plot(x, gaus, color=col, linewidth=2, linestyle=sty)

plt.legend(['Distr. 1', 'Distr. 2', 'Distr. 3'])
plt.tight_layout()
plt.savefig('desc_distr_chars.png')
