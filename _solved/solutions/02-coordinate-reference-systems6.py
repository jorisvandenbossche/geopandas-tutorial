# Convert the districts to the RGF93 reference system
districts_RGF93 = districts.to_crs(epsg=2154)  # or to_crs("EPSG:2154")