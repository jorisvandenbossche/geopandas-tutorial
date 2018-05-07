data_within_border = geopandas.sjoin(data_utm, protected_areas_border,
                                     op='within', how='inner')