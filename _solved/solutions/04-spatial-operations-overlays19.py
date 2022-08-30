land_use_muette['area'] = land_use_muette.geometry.area
# Total land use per class
land_use_muette.groupby("class")["area"].sum()