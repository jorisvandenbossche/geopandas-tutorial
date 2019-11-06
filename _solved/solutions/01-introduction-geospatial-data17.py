# Add a population density column
districts['population_density'] = districts['population'] / districts.geometry.area * 10**6