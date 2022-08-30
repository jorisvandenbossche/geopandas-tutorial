land_use_muette = land_use.copy()
land_use_muette['geometry'] = land_use.geometry.intersection(muette)
land_use_muette = land_use_muette[~land_use_muette.is_empty]
land_use_muette.head()