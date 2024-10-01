# import libraries and define global settings
import matplotlib.pyplot as plt
# define global figure properties used for publication
import matplotlib_inline.backend_inline
import numpy as np

matplotlib_inline.backend_inline.set_matplotlib_formats('svg')  # display figures in vector format
plt.rcParams.update({'font.size': 14,  # font size
                     'savefig.dpi': 300,  # output resolution
                     'axes.titlelocation': 'left',  # title location
                     'axes.spines.right': False,  # remove axis bounding box
                     'axes.spines.top': False,  # remove axis bounding box
                     })

x = [4, 5, 7]

# softmax transformation
num = np.exp(x)
den = np.sum(np.exp(x))
sigma = num / den

print(sigma)

# table data
colLabs = ['Raw', 'Softmax']

tabdat = []
for xi, si in zip(x, sigma):
    tabdat.append([f'{xi:.0f}', f'{si:.3f}'])

# draw the table
fig, ax = plt.subplots(figsize=(2.7, 3))
ax.set_axis_off()
ht = ax.table(
    cellText=tabdat,
    colLabels=colLabs,
    colColours=[(.8, .8, .8)] * len(colLabs),
    cellLoc='center',
    loc='upper left',
)

# some adjustments to the fonts etc
ht.scale(1, 3.8)
ht.auto_set_font_size(False)
ht.set_fontsize(14)

from matplotlib.font_manager import FontProperties

for (row, col), cell in ht.get_celld().items():
    cell.set_text_props(fontproperties=FontProperties(family='serif'))
    if row == 0: cell.set_text_props(fontproperties=FontProperties(weight='bold', size=16))

# export
plt.tight_layout()
plt.savefig('prob_table_softmax.png', bbox_inches='tight')

# the data (marble color counts)
counts = np.array([40, 30, 20])

# softmax
num = np.exp(counts)
den = np.sum(np.exp(counts))
sigma = num / den

# standard probabilities
probs = 100 * counts / np.sum(counts)

# print the results
print('Softmax:')
print(sigma)

print(' ')
print('Probabilities:')
print(probs)


