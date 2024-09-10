import numpy as np
from matplotlib import pyplot as plt

mongooses = np.arctanh(np.random.uniform(-.75, .75, size=500)) * 15 + 40

_, axs = plt.subplots(1, 2, figsize=(8, 3))

axs[0].hist(mongooses, bins=3, color='gray', edgecolor='k')
axs[0].set_title(r'$\bf{A}$)  Histogram with 3 bins')

axs[1].hist(mongooses, bins=300, color='gray', edgecolor='k')
axs[1].set_title(r'$\bf{B}$)  With 300 bins')

# stylizing
for a in axs:
    a.set_xlabel('Length (cm)')
    a.set_ylabel('Count')

plt.tight_layout()
plt.savefig('vis_mongeese_binoptions.png')
