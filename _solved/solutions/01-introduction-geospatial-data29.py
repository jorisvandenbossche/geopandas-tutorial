fig, ax = plt.subplots(figsize=(20, 10))
districts.plot(ax=ax, color='grey', alpha=0.4, edgecolor='k')
stations.plot(ax=ax, column='available_bikes', legend=True)
ax.set_axis_off()