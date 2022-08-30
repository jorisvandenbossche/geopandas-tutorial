# Make of map of the districts colored by 'n_trees_per_area'
ax = districts_trees.plot(column='n_trees_per_area', figsize=(12, 6))
ax.set_axis_off()