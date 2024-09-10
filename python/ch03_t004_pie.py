from matplotlib import pyplot as plt

mostNews = [15, 5, 70, 10]
source_labels = ['TV', 'Newspapers', 'Internet', 'Word of mouth']

# make the pie chart
plt.figure(figsize=(6.3, 6.3))
plt.pie(mostNews, labels=source_labels, autopct='%.0f%%', radius=1.2, wedgeprops={'edgecolor': 'k'})

plt.tight_layout()
plt.savefig('vis_pie.png')
