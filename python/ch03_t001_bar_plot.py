import matplotlib.pyplot as plt

news_sources = [40,10,85,20]
source_labels = ['TV','Newspapers','Internet','Word of mouth']

# show the bar plot
plt.figure(figsize=(8,3.3))
plt.bar(source_labels,news_sources,color=[.2,.2,.2])

# make the graph look a bit nicer
plt.title('Where do people get their news?',loc='center')
plt.ylabel('Percent responding "yes"')
plt.xlabel('Media type')
plt.xticks(rotation=-30)

plt.savefig('vis_barplot_news1.png',bbox_inches='tight')