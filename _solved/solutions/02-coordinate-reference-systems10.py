# Convert to the Web Mercator projection
stations_webmercator = stations.to_crs(epsg=3857)
stations.head()