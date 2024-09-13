# generate some data
import numpy as np
from matplotlib import pyplot as plt

# try on pdf to comapre with analytic
x = np.linspace(-8, 8, 1001)
s = 1.9

# create the Gaussian and compute its analytic FWHM
pureGaus = np.exp((-x ** 2) / (2 * s ** 2))
fwhm = 2 * s * np.sqrt(2 * np.log(2))

plt.figure(figsize=(10, 6))

# plot guide lines
plt.plot(x[[0, -1]], [.5, .5], '--', color=(.9, .9, .9))
plt.plot(x[[0, -1]], [1, 1], '--', color=(.9, .9, .9))
plt.plot(x[[0, -1]], [0, 0], '--', color=(.9, .9, .9))
plt.plot([0, 0], [0, 1], '--', color=(.9, .9, .9))
plt.plot([-fwhm / 2, -fwhm / 2], [0, .5], '--', color=(.5, .5, .5))
plt.plot([fwhm / 2, fwhm / 2], [0, .5], '--', color=(.5, .5, .5))

# plot the gaussian
plt.plot(x, pureGaus, 'k', linewidth=3)

# plot arrows
plt.arrow(-fwhm / 2, .5, fwhm, 0, color=(.5, .5, .5), linewidth=2, zorder=10,
          head_width=.05, head_length=.5, length_includes_head=True)
plt.arrow(fwhm / 2, .5, -fwhm, 0, color=(.5, .5, .5), linewidth=2, zorder=10,
          head_width=.05, head_length=.5, length_includes_head=True)

plt.text(0, .52, 'FWHM', horizontalalignment='center', fontsize=20)
plt.xlim(x[[0, -1]])
plt.yticks([0, .5, 1], labels=['0%', '50%', '100%'])
plt.ylabel('Gain')
plt.title(f'FWHM = {fwhm:.2f}', loc='center')

plt.tight_layout()
plt.savefig('desc_FWHM_def.png')
