data_within_protected = geopandas.sjoin(data_utm, protected_areas_utm[['NAME_AP', 'geometry']],
                                        op='within', how='inner')