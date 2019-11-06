# Spatial join of the trees and districts datasets
joined = geopandas.sjoin(trees, districts, op='within')
joined.head()