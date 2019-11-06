# Calculate the total area for each land use class
total_area = land_use.groupby('class')['area'].sum() / 1000**2
total_area