protected_areas = geopandas.read_file("data/Conservation/RDC_aire_protegee_2013.shp")
# or to read it directly from the zip file:
# protected_areas = geopandas.read_file("/Conservation", vfs="zip://./data/cod_conservation.zip")