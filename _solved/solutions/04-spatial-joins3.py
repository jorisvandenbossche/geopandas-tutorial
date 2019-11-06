# Read the trees and districts data
trees = geopandas.read_file("data/paris_trees.gpkg")
districts = geopandas.read_file("data/paris_districts.geojson").to_crs(trees.crs)