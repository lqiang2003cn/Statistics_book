import numpy as np
from matplotlib import pyplot as plt

# fake data
data = {
    'Horror': 8,
    'Romcom': 1,
    'Scifi': 9,
    'Action': 7,
    'Anime': 3,
    'Docu': 6
}

# angles for plotting
theta = np.linspace(0, 2 * np.pi, len(data) + 1)

# repeat first data point so the line wraps around
ratings = list(data.values())
ratings.append(ratings[0])

## draw the data
ax = plt.subplot(111, polar=True)
ax.plot(theta, ratings, 'ko-')
ax.fill(theta, ratings, 'k', alpha=.1)

# make the plot look nicer
ax.set_xticks(theta[:-1])
ax.set_xticklabels(data.keys())
ax.set_yticks([5, 10])
ax.set_ylim([0, 10])
ax.set_title('Movie genre preferences', y=1.1, loc='center')

plt.tight_layout()
plt.savefig('vis_radialBad.png')
