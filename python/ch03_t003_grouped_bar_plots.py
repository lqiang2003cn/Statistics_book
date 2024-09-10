import numpy as np
from matplotlib import pyplot as plt

source_labels = ['TV', 'Newspapers', 'Internet', 'Word of mouth']

news_sources = np.array([[12, 17, 95, 35],
                         [90, 40, 50, 25]])
agegroups = ['Millennials', 'Boomers']

_, axs = plt.subplots(1, 2, figsize=(10, 5))

axs[0].bar(np.arange(4) - .2, news_sources[0], width=.4, color='k')
axs[0].bar(np.arange(4) + .2, news_sources[1], width=.4, color='gray')
axs[0].set(xlabel='Media type', ylabel='Percentage responding "yes"', xticks=np.arange(4))
axs[0].set_xticklabels(source_labels, rotation=-30)
axs[0].legend(agegroups)
axs[0].set_title(r'$\bf{A}$)  Grouped by news source')

offset = [-.3, -.1, .1, .3]
hatches = 'xo-|'  # "hatch" is the fill shape
for i in range(4):
    axs[1].bar(np.arange(2) + offset[i], news_sources[:, i], width=.2, hatch=hatches[i], color=[.8, .8, .8], edgecolor='k')

# Note about color: Unless you need grayscale, color is nicer-looking than hatches:
# for i in range(4): axs[1].bar(np.arange(2)+offset[i],news_sources[:,i],width=.2)

axs[1].set(xlabel='Generation', ylabel='Percentage responding "yes"', xticks=np.arange(2))
axs[1].set_xticklabels(agegroups)
axs[1].legend(source_labels, fontsize=10)
axs[1].set_title(r'$\bf{B}$)  Grouped by generation')

plt.tight_layout()
plt.savefig('vis_barplot_news2.png')
