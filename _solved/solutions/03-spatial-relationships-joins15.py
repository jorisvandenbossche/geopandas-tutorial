# Spatial join of the trees and districts datasets
joined = geopandas.sjoin(trees, districts, predicate='within')
joined.head()