# Convert to the Web Mercator projection
stations_webmercator = stations.to_crs("EPSG:3857")
stations.head()