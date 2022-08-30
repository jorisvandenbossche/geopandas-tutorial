# Relative percentage of land use classes
land_use_muette.groupby("class")["area"].sum() / land_use_muette.geometry.area.sum() * 100