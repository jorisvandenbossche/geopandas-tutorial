# Calculate the total area for each land use class
print(land_use_muette.groupby('class')['area'].sum() / 1000**2)