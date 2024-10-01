# import libraries and define global settings
import matplotlib.pyplot as plt
# define global figure properties used for publication
import matplotlib_inline.backend_inline
import numpy as np
from scipy import stats

matplotlib_inline.backend_inline.set_matplotlib_formats('svg')  # display figures in vector format
plt.rcParams.update({'font.size': 14,  # font size
                     'savefig.dpi': 300,  # output resolution
                     'axes.titlelocation': 'left',  # title location
                     'axes.spines.right': False,  # remove axis bounding box
                     'axes.spines.top': False,  # remove axis bounding box
                     })

k = 20
t = np.tile(1 / k, k)
print(t)

_, axs = plt.subplots(2, 1, figsize=(4, 6))

for a, k in zip(axs, [2, 6]):

    # draw the pie (and export the patches and text to update the color)
    patches, _, autotexts = a.pie(np.tile(1 / k, k), autopct='%.1f%%', wedgeprops={'edgecolor': 'k'},
                                  colors=np.linspace((.2, .2, .2), (1, 1, 1), k))

    for autotext, patch in zip(autotexts, patches):
        inverse_color = 1 - np.array(patch.get_facecolor())
        inverse_color[-1] = 1  # invert the color, but not the alpha
        autotext.set_color(inverse_color)

axs[0].set_title('Coin flip', y=.9)
axs[1].set_title('Die roll', y=.9)

plt.tight_layout()
plt.savefig('prob_probsInPies.png')
