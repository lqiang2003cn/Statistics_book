from matplotlib import pyplot as plt

Y = [1, 4, 3, 9]  # bar heights
X = [0, 1, 3, 4]  # bar locations

plt.figure(figsize=(5, 2.5))
plt.bar(X, Y, color='k')
plt.xlabel('X')
plt.ylabel('Y')
plt.savefig('vis_barplot_basic.png')
