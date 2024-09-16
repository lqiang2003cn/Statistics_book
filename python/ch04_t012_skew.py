# generate some data
from matplotlib import pyplot as plt

colLabs = ['Moment number', 'Name', 'Description', 'Formula']

tableData = [['First', 'Mean', 'Average', r'$m_1 = N^{-1}\sum_{i=1}^N x_i$'],
             ['Second', 'Variance', 'Dispersion', r'$m_2 = N^{-1}\sum_{i=1}^N (x_i-\bar{x})^2$'],
             ['Third', 'Skew', 'Asymmetry', r'$m_3 = (N\sigma^3)^{-1}\sum_{i=1}^N (x_i-\bar{x})^3$'],
             ['Fourth', 'Kurtosis', 'Tail fatness', r'$m_4 = (N\sigma^4)^{-1}\sum_{i=1}^N (x_i-\bar{x})^4$']
             ]

# draw the table
fig, ax = plt.subplots(figsize=(10, 4))
ax.set_axis_off()
ht = ax.table(
    cellText=tableData,
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
    if col < 3 and row > 0: cell.set_text_props(fontproperties=FontProperties(size=16))

# export
plt.tight_layout()
plt.savefig('desc_table_moments1.png', bbox_inches='tight')
