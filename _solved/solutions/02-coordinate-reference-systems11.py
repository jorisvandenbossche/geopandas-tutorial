# Plot the stations with a background map
import contextily
ax = stations_webmercator.plot(markersize=5)
contextily.add_basemap(ax)