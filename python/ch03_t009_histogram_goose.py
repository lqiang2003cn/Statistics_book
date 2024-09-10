import numpy as np
from matplotlib import pyplot as plt

mongooses = np.arctanh(np.random.uniform(-.75, .75, size=500)) * 15 + 40

plt.figure(figsize=(8, 4))
plt.hist(mongooses, bins=30, color='gray', edgecolor='k')

plt.xlabel('Length (cm)')
plt.ylabel('Count')
plt.title('Lengths of Babylonian mongooses', loc='center')

plt.tight_layout()
plt.savefig('vis_mongeese.png')
