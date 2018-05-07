# alternative with constructing the matplotlib figure first
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(aspect='equal'))
protected_areas_utm.plot(ax=ax, color='green')
data_utm.plot(ax=ax, markersize=5, alpha=0.5)
ax.set_axis_off()