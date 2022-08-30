# Import the land use dataset
land_use = geopandas.read_file("data/paris_land_use.zip")
land_use.head()